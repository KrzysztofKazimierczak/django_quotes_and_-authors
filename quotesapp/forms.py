from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, DateField, DateInput
from .models import Tag, Quote, Author

class TagForm(ModelForm):

    tag = CharField(min_length=3, max_length=20, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']

class QuoteForm(ModelForm):

    author = ModelChoiceField(queryset=Author.objects.all(), required=True)
    content = CharField(min_length=3, max_length=500, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['author', 'content']
        exclude = ['tags']

class AuthorForm(ModelForm):

    name = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    born_date = DateField(widget=DateInput(attrs={'type': 'date'}))
    born_location = CharField(min_length=3, max_length=50)
    description = CharField(max_length=255)

    class Meta:
        model = Author
        fields = ['name','born_date','born_location','description']