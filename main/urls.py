from django.urls import path
from . import views

urlpatterns= [
    path('function', views.hello_world, name="hello"),
    path('class', views.HelloBro.as_view(), name="hellobro"),
    path('reservation', views.form, name="form"),
    path('', views.landing, name="landing"),
    path('menu', views.menu, name='menu'),
    path('view-reservations', views.showreservations, name="showreservations")
]