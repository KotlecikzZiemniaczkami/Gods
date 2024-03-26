from django.shortcuts import render
from django.http import HttpResponse

# view which will have list of gods
# btw if it's first view there is need to make new file "urls.py"
def aphrodite(request):
    return HttpResponse("Aphrodite sends kiss to You")
