from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# view which will have list of gods
# btw if it's first view there is need to make new file "urls.py"
def aphrodite(request):
    return HttpResponse("Aphrodite sends kiss to You")

def artemis(request):
    return HttpResponse("Artemis wishes you successful hunting")

def ares(request):
    return HttpResponse("Muuum, Hephaestus has stolen my knifeee!")

def athena(request):
    return HttpResponse("Ares is an idiot")

def antena(request):
    return HttpResponse("signal makes ziuuuuuu")

# it is possible to work with arguments.
def is_it_your_name(request, name):
    if len(name) < 5:
        text = 'Is ' + name + ' Your name? It is nice ;)'
        return HttpResponse(text)
    else:
        return HttpResponseNotFound('404')