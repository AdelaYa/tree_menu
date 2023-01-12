from django.contrib import admin
from django.urls import path
from tree_menu.views import MenuItemListView, MenuByMenuItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuItemListView.as_view(), name='menu-item-list'),
    path('<str:slug>/', MenuByMenuItemView.as_view(), name='item-by-category'),
]


