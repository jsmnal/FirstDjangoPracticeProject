from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image, Album

# luodaan rekisteröitymislomake
class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


# luodaan lomake kuvan lisäämiseen
class ImageAddForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image_name", "image_description", "album", "image"]


# luodaan lomake albumin lisäämiseen
class AlbumAddForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["album_name"]


# luodaan lomake kuvien poistamiseen
class DeleteImages(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image_name", "album"]
