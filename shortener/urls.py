from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='main_page'),
    path('<str:short_url>/', views.shortcut, name='shortcut')
]
