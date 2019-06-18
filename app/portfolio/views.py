from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, you are at my landing page.</h1>")
