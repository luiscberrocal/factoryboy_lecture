from django.http import HttpResponseRedirect, HttpRequest, HttpResponse


def change_theme(request: HttpRequest) -> HttpResponse:
    """Change the theme of the application."""
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = False
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
