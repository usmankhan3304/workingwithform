from django.forms import ModelForm
from django import forms
from .models import Student
class StudenRegisrationForm(ModelForm):
    name=forms.CharField(max_length=120, required=False)
    class Meta:
        model=Student
        fields='__all__'
        labels={'name':'Enter Your name','email':'Enter An Email'}
        error_messages={'name':{'required':'name required'},}
        widgets = {
            'password': forms.PasswordInput(render_value=True),
            'name':forms.TextInput(attrs={'class':'myclss',
                                          'placeholder':'enter name'})
        }