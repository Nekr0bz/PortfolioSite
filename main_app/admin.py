# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    """
    Управление данными о проектах
    """
    list_display = ['title']
    fields = ('title', 'description', 'img', 'site_link', 'github_link')


admin.site.register(Projects, ProjectsAdmin)


