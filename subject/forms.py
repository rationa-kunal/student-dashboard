from django import forms


class addLinkForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    contributor = forms.CharField(max_length=100)
    link = forms.URLField()




class addTagForm(forms.Form):

    choices = [('IP','imp'), ('PP','practical program'), ('PT','practical theory'), ('BF','by faculty'), ('VV','verified'), ('CL','cool'), ('GH','good handwriting')]
    title = forms.ChoiceField(choices=choices)