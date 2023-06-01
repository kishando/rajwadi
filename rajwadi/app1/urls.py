from django.urls import path
from app1  import views
from . import views

urlpatterns = [
   # path('app1/', views.app1, name='app1'),
     path('',views.login,name='login'),
     path('reg/',views.register,name='reg'),
     path('home/',views.home,name='home'),
     path('logout/',views.logoutpage,name='logout'),
     path('forgot/',views.forgot,name="forgot"),
     path('home/profile/', views.user_profile, name='user_profile'),
     path('updateprofile/',views.update_profile, name='updateprofile'),
     
]