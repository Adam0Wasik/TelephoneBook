from django import forms

class AddForm(forms.Form):
    name = forms.CharField(required=True,widget= forms.TextInput
                           (attrs={'placeholder':'First name'}))
    surname = forms.CharField(required=True,widget= forms.TextInput
                           (attrs={'placeholder':'Last name'}))
    number = forms.CharField(required=False,widget= forms.TextInput
                           (attrs={'placeholder':'Phone number'}))
    email = forms.CharField(required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Email address'}))

class SearchForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput
                            (attrs={'placeholder': 'First name'}))
    surname = forms.CharField(required=False, widget=forms.TextInput
                            (attrs={'placeholder': 'Last name'}))
    number = forms.CharField(required=False, widget=forms.TextInput
                            (attrs={'placeholder': 'Phone number'}))
    email = forms.CharField(required=False, widget=forms.TextInput
                            (attrs={'placeholder': 'Email address'}))

class AddNumberForm(forms.Form):
    number = forms.CharField(required=True, widget=forms.TextInput
                            (attrs={'placeholder': 'Phone number'}))

class AddEmailForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput
                           (attrs={'placeholder': 'Email address'}))
class EditForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput
                           (attrs={'placeholder': 'First name'}))
    surname = forms.CharField(required=False, widget=forms.TextInput
                           (attrs={'placeholder': 'Last name'}))
