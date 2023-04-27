from django.contrib import admin
from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
