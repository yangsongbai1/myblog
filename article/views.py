from django.shortcuts import render


def index(request):
    return render(request, 'article/index.html')


def learn(request):
    return render(request, 'article/list.html')


def about(request):
    return render(request, 'article/about.html')


def guestbook(request):
    return render(request, 'article/gbook.html')
