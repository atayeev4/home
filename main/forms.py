from django import forms


class UserData(forms.Form):    
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()


    
