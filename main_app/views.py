# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from models import Projects
from forms import ContactMessageForm


class MainPageView(ListView):
    """
    Представление отвечающее
    за главную страницу сайта
    """
    model = Projects
    template_name = 'main_app/index.html'
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
            'subject': 'Сообщение из моего сайта-визитки',
            'message': request.POST['message']
        }
        self.form = ContactMessageForm(form_data)

        if self.form.is_valid():
            self.form.send_email()
            success_msg = 'Спасибо за ваше письмо!'
            messages.add_message(self.request, messages.SUCCESS, success_msg)

        else:
            messages.add_message(self.request, messages.ERROR, self.form.errors.values()[0][0])

        return redirect(reverse_lazy('main')+'#footer')


