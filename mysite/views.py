from django.shortcuts import render


def index(request):
    return render(request, 'mysite/index.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    return render(request, 'mysite/contact.html')
