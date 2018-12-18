# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from models import Projects


class MainPageView(ListView):
    """
    Представление отвечающее
    за главную страницу сайта
    """
    model = Projects
    template_name = 'main_app/main.html'


