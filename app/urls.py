from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', home , name="home"),
    path('login/', login , name="login"),
    
]
