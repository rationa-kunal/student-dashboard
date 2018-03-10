from django import forms


class addLinkForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    contributor = forms.CharField(max_length=100)
    link = forms.URLField()