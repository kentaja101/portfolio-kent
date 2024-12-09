from django.shortcuts import render

def index(request):
    template = 'mainpages/resume.html'

    return render(request, template, {'is_homepage': False})