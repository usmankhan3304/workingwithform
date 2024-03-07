from django.shortcuts import render,HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=='POST':
      fm=UserRegistrationForm(request.POST)
      if fm.is_valid():
         fm.save()
         messages.success(request, 'Registered Successfully!.')
         fm=UserRegistrationForm()
    else:
      fm=UserRegistrationForm()
        
    return render(request,'enroll/signup.html',{'form':fm})