from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/<int:pk>/', DetailEventView.as_view(), name='event_detail'),
    path('collection/<int:pk>/', DetailCollectionView.as_view(), name='collection_detail'),
    path('event-by-category/<int:pk>/', DetailCategoryView.as_view(), name='category_detail'),
    path('all-colletions/', ListCollectionsView.as_view(), name='collection_list'),
    path('all-cats/', ListCategoriesView.as_view(), name='list_cats'),
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
    path('registr_event/<int:pk>/', registr_event_view, name='registr_event'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
