from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='main_page'),
    path('<str:shortcut>/', views.shortcut, name='shortcut')
]
