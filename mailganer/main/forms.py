from .models import Mail
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, CheckboxInput, ChoiceField


class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ['mail', 'message', 'checkbox', 'date']

        widgets = {
            'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кому'
            }),
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст сообщения'
            }),
            'checkbox': CheckboxInput(

            ),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата отправки сообщения'
            }),
        }