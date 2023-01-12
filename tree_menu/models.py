from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='Название',
    )
    items =  models.ForeignKey(
        'MenuItem',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='items',
        verbose_name='Элементы меню')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(MPTTModel):
    menu_name = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name='Название меню')
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        verbose_name='Родительская категория',
        related_name='child',
        db_index=True,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length = 150,
        verbose_name='Название элемента меню'
    )
    slug = models.SlugField(
        verbose_name='url',
        blank=True,
        null=True,
    )

    class MPTTMeta:
        order_insertion_by = ['name',]

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def get_absolute_url(self):
        return f'/{self.slug}'

    def __str__(self):
        return self.name


