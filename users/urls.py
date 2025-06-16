from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/<int:pk>/', DetailEventView.as_view(), name='event_detail'),
]
