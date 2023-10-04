from django import forms

class Registform(forms.Form):
    firstname=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    file=forms.FileField()
    phone=forms.IntegerField()
    pin=forms.IntegerField()
    repin=forms.IntegerField()

class Logform(forms.Form):
    username=forms.CharField(max_length=30)
    pin=forms.IntegerField()

class newsform(forms.Form):
    topic=forms.CharField(max_length=50)
    content=forms.CharField(max_length=100)


class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)


