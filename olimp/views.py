from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# "in Django you can't just read template. You should convert it into string" this is for what you want render_to_string in your code
from django.template.loader import render_to_string

# answers given by gods
god_answers = {
    "zeus": "gimme coffee",
    "hera": "gimme tea",
    "athena": "wanna play chess?",
    "antena": "you have fu*kn project to do!",
    "artemis": "Do you want to relax by the fireplace? I have roasted wild boar"
}

def accessible_gods(request):
    httext = ''
    a_gods = list(god_answers.keys())
    for i in range(len(a_gods)):
        httext = httext + str(i+1) + '.' + f'<a href="{reverse("god-says", args=[a_gods[i]])}">' + a_gods[i].capitalize() + "</a><br>"
    return HttpResponse(httext)

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
        return HttpResponse(render_to_string("olimp/gods_reaction.html"))
    # or not
    except:
        return HttpResponseNotFound("404\ngod not found")