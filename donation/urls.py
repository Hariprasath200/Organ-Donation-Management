from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('donar',views.donar,name='donar'),
    path('adminn',views.admin,name='adminn'),
    path('receiver',views.receiver,name='receiver'),
]