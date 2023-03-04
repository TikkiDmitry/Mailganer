# coding=utf-8
from django.shortcuts import render
from .forms import MailForm
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from .models import Mail
from .data import SENDER, PASSWORD
# send_mail_task.apply_async(
#    (('noreply@example.com', ), 'Celery cookbook test', 'test', {}),
#    eta=datetime(2019, 5, 20, 7, 0)


def index(request):
    error = ''

    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data.get('mail')
            message = form.cleaned_data.get('message')
            checkbox = form.cleaned_data.get('checkbox')
            # date = form.cleaned_data.get('date')

            # Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
            # if date < datetime.date.today():
            #     raise ValidationError(_('Invalid date - renewal in past'))

            print(mail, message, checkbox)

            if checkbox == True:
                pass
            # КАК ПО ЧЕКБОКСУ ОТОБРАЗИТЬ СКРЫТОЕ ПОЛЕ ФОРМЫ И КАК ЗАПИСАТЬ ДАННЫЕ В БД НЕ ИЗ ФОРМЫ

            if "@gmail.com" in mail:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()

                sender = SENDER
                password = PASSWORD
                try:
                    server.login(sender, password)
                    server.sendmail(sender, mail, MIMEText(message).as_string())
                except Exception as _ex:
                    return _ex
                form.save()
            else:
                error = 'Неверно заполнен адрес электронной почты'

    form = MailForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/index.html', data)