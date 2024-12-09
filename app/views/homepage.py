from django.shortcuts import render

def index(request):
    template = 'mainpages/homepage.html'

    return render(request, template, {'is_homepage': True})

def all(request):
    template = 'mainpages/homepage12.html'

    return render(request, template, {'is_homepage': True})