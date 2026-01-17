from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# class UploadPost_ItemForm(forms.Form):
#     text = forms.CharField()
#     image = forms.FileField(required=False)
#     file = forms.FileField(required=False)
# class ProfileForm(forms.Form):
    icon = forms.FileField(required=False)
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=1000)