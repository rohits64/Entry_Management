from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('host/new/',views.host_new,name='host_new'),
    path('visitor/new/',views.visitor_new,name='visitor_new'),
    path('visitor/check_out/',views.visitor_out,name='visitor_out'),
]