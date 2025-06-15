from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "age", "is_staff"]

class EventAdmin(admin.ModelAdmin):
    model = EventModel
    list_display = ["name"]

class CollectionsAdmin(admin.ModelAdmin):
    model = CollectionsModel
    list_display = ["event"]


class CategoryAdmin(admin.ModelAdmin):
    model = CategoryModel
    list_display = ["name"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EventModel, EventAdmin)
admin.site.register(CollectionsModel, CollectionsAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
