from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def shortcut(request):
    return render(request, 'index.html')
