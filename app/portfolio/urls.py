from django.urls import path

from . import views

urlpatterns = [
    # /portfolio/
    path('', views.index, name='index'),
    # /portfolio/<menu_item>
    path('<str:menu_item>/', views.detail, name='detail'),
]
