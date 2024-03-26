from django.urls import path
from . import views

# list of our views :]
# to work there is need to import a path function
# first argument is what will be in url, the second one is which function/class
# should be executed when it is triggered
urlpatterns = [
    path('aphrodite', views.aphrodite),
    path('artemis', views.artemis),
    path('ares', views.ares),
    path('athena', views.athena),
    path('antena', views.antena),
    path('<name>', views.is_it_your_name)
]
# now there is created sth called "url config"