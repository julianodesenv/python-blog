from django.forms import ModelForm
from .models import Comment

class FormComment(ModelForm):

    def clean(self):
        data = self.cleaned_data

        name = data.get('name')
        email = data.get('email')
        comment = data.get('comment')

        if len(name) < 5:
            self.add_error(
                'name',
                'Nome precisa ter mais que 5 caracteres.'
            )


    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')