# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Projects(models.Model):
    """
    Модель работ
    """
    title = models.CharField('Заголовок', max_length=80)
    description = models.TextField('Краткое описание', max_length=200)
    img = models.ImageField(upload_to='projects/', verbose_name='Превью', help_text='270x270px')
    site_link = models.URLField('Ссылка на сайт', blank=True)
    github_link = models.URLField('Ссылка на github', blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        db_table = 'Projects'

    def __unicode__(self):
        """
        Строковое представление объекта
        """
        return self.title
