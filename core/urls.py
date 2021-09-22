from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView, name='Home'),
    path('api/', dataAPIView.as_view())
]