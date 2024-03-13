from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Video, News, Live


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current_password', 'class': 'form-control'}))


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'video_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Check if required fields are empty
        required_fields = ['title', 'thumbnail', 'video_url', 'video_date', 'video_type']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, 'This field is required')

        return cleaned_data


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Check if required fields are empty
        required_fields = ['title', 'subtitle', 'poster', 'para1', 'para2', 'para3', 'para4', 'para5', 'date']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, 'This field is required')

        return cleaned_data


class LiveForm(forms.ModelForm):
    class Meta:
        model = Live
        fields = '__all__'
        widgets = {
            'video_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Check if required fields are empty
        required_fields = ['title', 'thumbnail', 'video_url', 'video_date']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, 'This field is required')

        return cleaned_data
