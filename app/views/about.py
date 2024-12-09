from django.shortcuts import render

def index(request):
    template = 'mainpages/about.html'

    return render(request, template, {'is_homepage': False})