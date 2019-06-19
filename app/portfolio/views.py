from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, you are at my landing page.</h1>")

def detail(request, menu_item):
    return HttpResponse("<h2>Content for menu item %s.</h2>" % menu_item)
