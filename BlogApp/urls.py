from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('unlog', views.unlog, name='unlog'),
    path('create', views.createblog, name='create'),
    path('success', views.succeess, name='success_page'),
]