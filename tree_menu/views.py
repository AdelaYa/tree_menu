from django.views.generic import ListView
from .models import Menu, MenuItem


class MenuItemListView(ListView):
    model = Menu
    template_name = "templates/base.html"


class MenuByMenuItemView(ListView):
    context_object_name = 'menu_items'
    template_name = 'templates/menu.html'

    def get_queryset(self):
        self.menu_item = MenuItem.objects.get(slug=self.kwargs['slug'])
        self.menu_item_values = MenuItem.objects.filter(name=self.menu_item).values()
        self.menu_item_level = self.menu_item_values[0]['level']
        self.family = [str(x) for x in self.menu_item.get_family()]

        menu_name_id = self.menu_item_values[0]['menu_name_id']
        queryset = MenuItem.objects.filter(
            menu_name_id=menu_name_id,
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['level'] = self.menu_item_level
        context['name'] = str(self.menu_item)
        context['family'] = self.family
        return context