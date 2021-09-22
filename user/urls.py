from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('signup/', registerView, name='signup'),
    path('logout/', logoutView, name='logout')
]