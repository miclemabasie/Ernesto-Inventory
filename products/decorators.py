from django.http import HttpResponseBadRequest


def require_post(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method != "POST":
            return HttpResponseBadRequest("Only POST requests are allowed.")
        return view_func(request, *args, **kwargs)

    return wrapper
