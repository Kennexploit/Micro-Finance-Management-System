from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register_view, name='register'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('loan/', views.Loan, name='loan'),
path('approved/', views.approvedLoans, name='approved'),
path('search/', views.search, name='search')

]