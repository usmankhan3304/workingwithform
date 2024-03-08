from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EditUserProfile,EditAdminProfile
from django.contrib.auth.models import User
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
def login_page(request):
    if  request.user.is_authenticated:
        return HttpResponseRedirect ('/reg/success/') 
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"loged in")
                return HttpResponseRedirect ('/reg/success/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'enroll/login.html', {'form': form})
@login_required(login_url='/reg/login/')
def success_page(request):
    if request.method == 'POST':
        if request.user.is_superuser:
           form=EditAdminProfile(request.POST, instance=request.user)
           users=User.objects.all()

        else:  
          form = EditUserProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
           
            messages.success(request,"updated successfylly!")
            return HttpResponseRedirect('/reg/success/')
    else:
        if request.user.is_superuser==True:
          form=EditAdminProfile(instance=request.user)
          users=User.objects.all()
        else:
          form = EditUserProfile(instance=request.user)
          users=None 
    return render(request, 'enroll/success.html',{"form":form,'useranme':request.user.username,'users':users})
def logout_view(request):
    logout(request)
    # Redirect the user to a logged out page or any desired page
    return redirect('login')
#change the password with the old one...
def ChangePassword(request):
    if request.user.is_authenticated:
      if request.method=="POST":
          fm=PasswordChangeForm(user=request.user,data =request.POST)
          
          if fm.is_valid():
              fm.save()
              update_session_auth_hash(request,fm.user)
              return HttpResponseRedirect('/reg/success/')
      else:
        fm=PasswordChangeForm(user=request.user)
        print(fm)
    
      return render(request,'enroll/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/reg/login/')
    #change password without old one..

def user_change_pass1(request):
    if request.user.is_authenticated:
      if request.method=="POST":
          fm=SetPasswordForm(user=request.user,data =request.POST)
          
          if fm.is_valid():
              fm.save()
              update_session_auth_hash(request,fm.user)
              return HttpResponseRedirect('/reg/success/')
      else:
        fm=SetPasswordForm(user=request.user)
        print(fm)
    
      return render(request,'enroll/changepassword1.html',{'form':fm})
    else:
        return HttpResponseRedirect('/reg/login/')
def userdetails(request,id):
   if request.user.is_authenticated:
      pi=User.objects.get(pk=id)
      form=EditAdminProfile(instance=pi)
      return render(request,'enroll/userdetails.html',{'form':form})