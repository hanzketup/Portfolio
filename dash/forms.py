from django import forms

class newPost(forms.Form):

    title = forms.CharField(label='title', max_length=200)
    pk = forms.CharField(label="pk", required=False)
    content = forms.CharField(label='content')
    cat = forms.CharField(label='cat', max_length=100)
