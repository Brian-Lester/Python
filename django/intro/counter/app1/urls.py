from django.urls import path     
from . import views

urlpatterns =[
    path('',views.index),
    path('destroy', views.destroy),
    path('plus2', views.plus2),
    path('plusnum',views.plusnum)
]