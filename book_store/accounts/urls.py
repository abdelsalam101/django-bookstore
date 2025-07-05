from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_pg, name='login'),
    path('logout/', views.signout, name='logout'),
]
