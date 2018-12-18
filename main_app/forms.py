
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.mail import send_mail


from portfoliosite import settings


class ContactMessageForm(forms.Form):
    """
    Форма для связи с администрацией сайта
    """
    name = forms.CharField(max_length=35, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    subject = forms.CharField(max_length=50, widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))

    error_css_class = 'error'

    def _generate_message(self):
        """
        Формирование сообщение администрации
        """
        subject = self.cleaned_data['subject']
        message = 'Name: ' + self.cleaned_data['name'] + '\n'
        message += 'Email: ' + self.cleaned_data['email'] + '\n'
        message += self.cleaned_data['message']
        return subject, message

    def send_email(self):
        """
        Отправка соощения администрации
        """
        (subject, message) = self._generate_message()
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['nekr0bz2@yandex.ru'])
