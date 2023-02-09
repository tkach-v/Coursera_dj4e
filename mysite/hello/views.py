from django.http import HttpResponse


# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)


def myview(request):
    value = request.COOKIES.get('dj4e_cookie', '61592633')
    resp = HttpResponse('In a view - the dj4e_cookie cookie value is ' + str(value) + '\n')
    resp.set_cookie('dj4e_cookie', '61592633', max_age=1000)

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del (request.session['num_visits'])
    resp = HttpResponse('In a view - the dj4e_cookie cookie value is ' + str(value) + ', ' + 'view count=' + str(num_visits))
    return resp
