from django import forms
from .models import Subscriber
from django.core.exceptions import ValidationError

class SubscriberForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            raise ValidationError("You're already subscribed with this email.")
        return email

class SubscriberModelForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            raise ValidationError("This email is already subscribed.")
        return email