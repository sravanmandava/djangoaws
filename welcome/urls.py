from django.urls import path
from welcome.views import index

urlpatterns = [
    path('home/<name>/', index, name='index')
]
