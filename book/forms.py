from .models import Booking, Tour
from django import forms

class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ('user', 'title', 'start_time')
    widgets = {
      'user': forms.TextInput(attrs={'id':'id', 'type':'hidden'}),
      'title': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
      'start_time': forms.DateInput(attrs={'type': 'datetime-local', 'class':'form-control'}, format='%Y-%m-%dT%H:%M'),
    }

class AddTravelForm(forms.ModelForm):
  class Meta:
    model = Tour
    fields = ('owner', 'title', 'image', 'body', 'price', 'flightfrom', 'flightto', 'days')
    widgets = {
      'owner': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'id', 'type':'hidden'}),
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'image': forms.FileInput(attrs={'class':'form-control'}),
      'body': forms.Textarea(attrs={'class':'form-control'}),
      'flightto': forms.TextInput(attrs={'class':'form-control'}),
      'price': forms.NumberInput(attrs={'class':'form-control'}),
      'days': forms.NumberInput(attrs={'class':'form-control'}),
    }