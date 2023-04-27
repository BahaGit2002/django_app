from django.db import models


class Menu(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    parent = models.ForeignKey('self', verbose_name='parent', related_name='menus', on_delete=models.CASCADE,
                               null=True, blank=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.title}'
