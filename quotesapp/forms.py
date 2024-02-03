from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quote

class TagForm(ModelForm):

    tag = CharField(min_length=3, max_length=20, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']

class QuoteForm(ModelForm):

    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    content = CharField(min_length=3, max_length=500, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['author', 'content']
        exclude = ['tags']
