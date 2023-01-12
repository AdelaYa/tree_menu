from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    prepopulated_fields =  {"slug": ("name",)}

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name',]
    list_display = ('name', )
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(DjangoMpttAdmin):
    prepopulated_fields =  {"slug": ("name",)}
    fields = ['name', 'menu_name', 'parent', 'slug']
    list_display = ('name', 'menu_name', 'parent','slug')

