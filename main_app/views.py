# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from models import Projects
from forms import ContactMessageForm


class MainPageView(ListView):
    """
    Представление отвечающее
    за главную страницу сайта
    """
    model = Projects
    template_name = 'main_app/main.html'
    form = None

    def get(self, request, *args, **kwargs):
        """
        Инициализация формы
        """
        self.form = ContactMessageForm()
        return super(MainPageView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Добавление формы в контекст
        """
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        """
        Отправка сообщения
        """
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message']
        }

        self.form = ContactMessageForm(form_data)
        if self.form.is_valid():
            self.form.send_email()

        return self.get(request, *args, **kwargs)


