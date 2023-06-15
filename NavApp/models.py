from django.db import models


class Site(models.Model):
    site_title = models.CharField(verbose_name='Заголовок (title)', max_length=255, default="Заголовок")
    site_nav = models.CharField(verbose_name='Название ссылки', max_length=255, default="Название ссылки")
    site_nav_position = models.IntegerField(verbose_name='Приоритет в навигации (0 - исключить)', default=0, )
    site_content = models.TextField(verbose_name='Основное содержание страницы',
                                    default='', blank=True)

    class Meta:
        verbose_name = 'Контент текущей страницы'
        verbose_name_plural = 'Уникальный контент страниц'
        ordering = ('-site_nav_position',)

    def __str__(self):
        return f"id: {self.id}.  {self.site_title}"
