from django.forms import ModelForm, TextInput, Textarea
from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        widgets = {
            'title': TextInput(attrs={'class': 'form-input'}),
            'content': Textarea(attrs={'cols': 60, 'rows': 10})
        }

