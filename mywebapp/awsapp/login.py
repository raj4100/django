from django import forms

class LoginForm(forms.Form):
    email=forms.EmailField(label='Email-ID:')
    password = forms.CharField(label='Password:', widget = forms.PasswordInput())

class SignUpForm(forms.Form):
    fname = forms.CharField(label='Full Name:')
    mobile = forms.DecimalField(label='Mobile:')
    email = forms.EmailField(label='Email-ID:')
    password = forms.CharField(label='Password:', widget = forms.PasswordInput())

class KeyForm(forms.Form):
    accountid = forms.CharField(label='accountid')
    accesskey = forms.CharField(label='accesskey')

class AwsInstance(forms.Form):
    amitype = forms.CharField(label='amitype')
    instancetype = forms.CharField(label='instancetype')
    instanceno = forms.IntegerField(label='instanceno')

class UnknownForm(forms.Form):
    iid = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
