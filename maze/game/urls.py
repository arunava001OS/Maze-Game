
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('signup/',views.signup,name='signup'),
	path('login/',views.login_view,name='login'),
	path('signout/',views.logout_view,name='logout'),
    path('playnow/',views.play,name = 'play'),

    path('game/',views.game,name='game'),
    path('game/playnow2/<key>',views.play2,name = 'play2'),
    path('auth/',include('social_django.urls',namespace = 'social')),

]
