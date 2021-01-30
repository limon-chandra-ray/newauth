from django.urls import path
from teacher import views

urlpatterns = [
    path('',views.home,name='home')
]
