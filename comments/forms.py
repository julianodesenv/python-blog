from django.forms import ModelForm
from .models import Comment
import requests

class FormComment(ModelForm):

    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': 'SUA CHAVE BACK END AQUI',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        print(recaptcha_result)
        print(recaptcha_result.get('success'))

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe Mr. Robot, ocorreu um erro.'
            )

        cleaned_data = self.cleaned_data

        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        comment = cleaned_data.get('comment')

        if len(name) < 5:
            self.add_error(
                'name',
                'Nome precisa ter mais que 5 caracteres.'
            )


    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')