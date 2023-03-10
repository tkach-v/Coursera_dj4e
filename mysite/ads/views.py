from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.urls import reverse_lazy
from django.views import View

from .forms import CreateForm, CommentForm
from .models import Ad, Comment
from .owner import *


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(View):
    def get(self, request, pk):
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = {'ad': x, 'comments': comments, 'comment_form': comment_form}
        return render(request, 'ads/ad_detail.html', context)


class AdCreateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('ads:all')

    def get(self, request):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, 'ads/ad_form.html', ctx)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'ads/ad_form.html', ctx)
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form': form}
        return render(request, 'ads/ad_form.html', ctx)

    def post(self, request, pk=None):
        ad = get_object_or_404(Ad, pk=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'ads/ad_form.html', ctx)
        ad = form.save(commit=False)
        ad.save()
        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad
    success_url = reverse_lazy('ads:all')


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        a = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=a)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])
