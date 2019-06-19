#Django
from django import forms

# Models
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Profile
        fields = ['user','phone_number','picture','first_name','last_name']

    def save(self):
        data = self.cleaned_data
        first_name = data['first_name']
        last_name = data['last_name']
        user = data['user']
        user.first_name = first_name
        user.last_name = last_name
        user.save()

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70)
    password_confirmation = forms.CharField(max_length=70)
    email = forms.CharField(min_length=6,max_length=70)
    phone_number = forms.CharField(min_length=10)

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Ya esta en uso el Username')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data
    

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        phone_number = data['phone_number']
        data.pop('password_confirmation')
        data.pop('phone_number')
        user = User.objects.create_user(**data)
        Profile.objects.create(user=user, phone_number=phone_number)
    

    
