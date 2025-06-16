from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/<int:pk>/', DetailEventView.as_view(), name='event_detail'),
    path('collection/<int:pk>/', DetailCollectionView.as_view(), name='collection_detail'),
    path('event-by-category/<int:pk>/', DetailCategoryView.as_view(), name='category_detail'),
    path('all-colletions/', ListCollectionsView.as_view(), name='collection_list'),
]
