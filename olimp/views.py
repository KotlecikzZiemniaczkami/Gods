from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# answers given by gods
god_answers = {
    "zeus": "gimme coffee",
    "hera": "gimme tea",
    "athena": "wanna play chess?",
    "antena": "you have fu*kn project to do!",
    "artemis": "Do you want to relax by the fireplace? I have roasted wild boar"
}

# mihological redirection
def god_hierarchy(request, ask):
    # we will take their names by hierarchy
    greek_god_hierarchy = list(god_answers.keys())
    try:
        return HttpResponseRedirect("/olimp/" + greek_god_hierarchy[ask])
    except:
        return HttpResponseNotFound("404\nsorry, god not found")

# god has spoken ;]
def god_says(request, ask):
    try:
        return HttpResponse(god_answers[ask])
    # or not
    except:
        return HttpResponseNotFound("404\ngod not found")