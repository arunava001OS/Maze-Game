
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('signup/',views.signup,name='signup'),
	path('login/',views.login_view,name='login'),
	path('signout/',views.logout_view,name='logout'),
]
