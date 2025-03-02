# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

def events(request):
    return render(request, 'events.html') 

def makerspace(request):
    return render(request, 'makerspace.html') 

def page2mk(request):
    return render(request, 'page2mk.html')

def page3mk(request):
    return render(request, 'page3mk.html')

def page2spk(request):
    return render(request, 'page2spk.html')

def page3spk(request):
    return render(request, 'page3spk.html')

def speakers(request):
    return render(request, 'speakers.html')

def faq(request):
    return render(request, 'faq.html') 





