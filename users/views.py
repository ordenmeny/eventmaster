from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import *

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
        context["soon_events"] = EventModel.objects.all() # Сделать фильтрацию по дате
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