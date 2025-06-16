from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from .forms import *

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomLoginForm
    extra_context = {
        'title': 'Войти',
    }

    def get_success_url(self):
        return reverse('users:home')




class HomePageView(TemplateView):
    template_name = 'users/home.html'
    extra_context = {
        'title': 'Ваша афиша. Главная страница',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context["message"] = "Добро пожаловать!"
        context["collections"] = CollectionsModel.objects.all()
        context["soon_events"] = EventModel.objects.all()  # Сделать фильтрацию по дате
        context["cats"] = CategoryModel.objects.all()
        return context


class DetailEventView(DetailView):
    model = EventModel
    template_name = 'users/event_detail.html'
    context_object_name = 'event'


class DetailCollectionView(DetailView):
    model = CollectionsModel
    template_name = 'users/collection_detail.html'
    context_object_name = 'collection'


class DetailCategoryView(ListView):
    model = EventModel
    template_name = 'users/category_detail.html'
    context_object_name = 'events'

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return EventModel.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.get(pk=self.kwargs['pk'])
        return context


class ListCollectionsView(ListView):
    model = CollectionsModel
    template_name = 'users/collection_list.html'
    context_object_name = 'collections'


class ListCategoriesView(TemplateView):
    template_name = 'users/cats_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = CategoryModel.objects.all()
        return context


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


@login_required
def registr_event_view(request, pk):
    event = get_object_or_404(EventModel, pk=pk)
    request.user.events.add(event)
    return redirect('users:user_profile')
