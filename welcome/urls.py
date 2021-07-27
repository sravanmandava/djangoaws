from django.urls import path
from welcome.views import saveToDb,hello

urlpatterns = [
    path('home/<name>/', hello, name='hello'),
    path('savetodb/<name>/', saveToDb, name='saveToDb'),
]
