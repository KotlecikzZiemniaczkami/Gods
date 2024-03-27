from django.urls import path
from . import views

# list of our views :]
# to work there is need to import a path function
# first argument is what will be in url, the second one is which function/class
# should be executed when it is triggered
urlpatterns = [
    path("<int:ask>", views.god_hierarchy),
    path("<str:ask>", views.god_says, name = "god-says"),
    path("", views.accessible_gods)
]
# now there is created sth called "url config"