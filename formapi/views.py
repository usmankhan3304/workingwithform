from django.shortcuts import render,HttpResponse
from .form import StudentRegistration
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def success(request):
     return HttpResponse("submitted successfully!")
def index(request):
    if request.method=="POST":
         form=StudentRegistration(request.POST)
         if form.is_valid():
              name=form.cleaned_data['name']
              print(name)
              return HttpResponseRedirect('/modelform/success/')
   
    else:
         form=StudentRegistration()
    return render(request,'modelform/index.html',{'form':form})
 