from django import forms
from .models import PostItem, Profile
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class PostItemForm(forms.ModelForm):
    class Meta:
        model = PostItem
        fields = ["text", "image", "video"]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_icon"]