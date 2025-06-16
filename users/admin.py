from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "age", "is_staff"]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "image",
                    "events"
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

class EventAdmin(admin.ModelAdmin):
    model = EventModel
    list_display = ["name"]

class CollectionsAdmin(admin.ModelAdmin):
    model = CollectionsModel
    list_display = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    model = CategoryModel
    list_display = ["name"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EventModel, EventAdmin)
admin.site.register(CollectionsModel, CollectionsAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
