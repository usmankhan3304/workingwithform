from django import forms
from django import forms

class StudentRegistration(forms.Form):
   
    error_css_class = "error required"
    name = forms.CharField(error_messages={"required": "Enter your name"})
    email = forms.EmailField(label_suffix=" ")

    