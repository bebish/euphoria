from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from fragnances.models import Fragnance, FragnanceComment, Favourite, ShoppingList
from subscribes.models import Subscribe
from users.models import User

@admin.register(Fragnance)
class FragnanceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'brand',
        'price',
        'size',
        'available',
        'rating'
    )

@admin.register(FragnanceComment)
class FragnanceCommentAdmin(admin.ModelAdmin):
    list_display = (
        'fragnance',
        'user',
        'text',
        'rating',
        'created_at'
    )

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'fragnance')

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'fragnance')


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    list_display_links = (
        "username",
        "email",
    )
    list_filter = ("username", "email")
    search_fields = ("username",)
    empty_value_display = "-пусто-"


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    """Админка подписок."""

    list_display = ("user", "author")
    list_editable = ("author",)
    list_display_links = ("user",)
    empty_value_display = "-пусто-"