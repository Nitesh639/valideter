from django.urls import path
from . import views

# here we map all the url links
urlpatterns = [
    path('', views.index,name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login,name='login'),
    path('user_status', views.user_status,name='user_status'),
    path('status', views.status,name='status'),
    path('email_check', views.email_check,name='email_check'),
]
