from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu


def index(request):
    menu = Menu.objects.order_by('order')
    context = {'menu_list': menu}
    return render(request, 'portfolio/index.html', context)

def detail(request, menu_item):
    return HttpResponse("<h2>Content for menu item %s.</h2>" % menu_item)
