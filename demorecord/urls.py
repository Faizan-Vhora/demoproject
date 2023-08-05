from django.urls import path
from .views import *

urlpatterns = [
   
    path('home/',home),
    path('datetime/',datetime1),
    path('index/',index),
    path('index2/',index2),
    path('veggi/',index3),
    path('create/',create),
]