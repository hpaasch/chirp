from django import forms

from main.models import Profile

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["favorite_bird", "photo"]
