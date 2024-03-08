from django.urls import path
from enroll import views
urlpatterns = [
    path('',views.signup,name="signup"),
    path('login/',views.login_page,name="login"),
    path('success/', views.success_page, name='success_page'),
    path('logout/', views.logout_view, name='logout'), 
    path("changepassword/",views.ChangePassword,name="changepassword"),
    path("changepass/",views.user_change_pass1,name="changepass"),
    path('user-details/<int:id>',views.userdetails,name="user_details")
]
