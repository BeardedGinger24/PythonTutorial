'''Defines URL patterns for users'''

from django.urls import path
from django.contrib.auth.views import login
from . import views

app_name = 'users'
urlpatterns = [
	# login page
	path('login/', login, {'template_name':'users/login.html'}, name='login'),
	# logout page
	path('logout/', views.logout_view, name = 'logout'),
	# Registration page
	path('register/', views.register, name = 'register'),
]