# render jus sends the html code as a response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# answers given by gods
god_answers = {
    "zeus": ["gimme coffee", "#FFFFE0"],
    "hera": ["gimme tea",  	"#FFFF00"],
    "athena": ["wanna play chess?", "#00CED1"],
    "antena": ["you have fu*kn project to do!", "#A9A9A9"],
    "artemis": ["Do you want to relax by the fireplace? I have roasted wild boar", "#228B22"]
}


def accessible_gods(request):
    httext = ''
    a_gods = list(god_answers.keys())
    
    return render(request, "olimp/choose_your_god.html", {"choose": a_gods})

# mihological redirection


def god_hierarchy(request, ask):
    # we will take their names by hierarchy
    greek_god_hierarchy = list(god_answers.keys())

    # reverse dynamically builds a path to url named as given, and gives it given argument
    redirect_path = reverse("god-says", args=[greek_god_hierarchy[ask]])
    return HttpResponseRedirect(redirect_path)

# god has spoken ;]


def god_says(request, ask):
    try:
        # it sends an html file (it needs to ad a request as an argument)
        return render(request, "olimp/gods_reaction.html", {
            "text": god_answers[ask][0],
            "color": god_answers[ask][1],
            "god_name": ask.capitalize()})
    # or not
    except:
        return HttpResponseNotFound("404\ngod not found")
