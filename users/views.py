from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
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

