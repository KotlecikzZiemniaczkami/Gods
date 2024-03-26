from django.urls import path
from . import views

# list of our views :]
# to work there is need to import a path function
# first argument is what will be in url, the second one is which function/class
# should be executed when it is triggered
urlpatterns = [
    path('aphrodite', views.aphrodite)
]
# now there is created sth called "url config"