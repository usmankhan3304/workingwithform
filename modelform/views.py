from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .form import StudenRegisrationForm
from  .models import Student
from django.contrib import messages

# Create your views here.
def success(request):
     return HttpResponse("submitted successfully!")
def register(request):
    pi=Student.objects.get(pk=2)
    if request.method == 'POST':
        form = StudenRegisrationForm(request.POST,)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            
            my_model_instance = Student(name=name, email=email, password=password)
            my_model_instance.save()
            messages.success(request, 'Registered Successfully!.')
            # form.save()#this is fo update
            form=StudenRegisrationForm()

            # return HttpResponseRedirect('/formapi/success/')
   
    else:
         form=StudenRegisrationForm()
    return render(request,'formapi/index.html',{'form':form})
       
     