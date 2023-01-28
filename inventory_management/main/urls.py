from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('', views.home, name='home'),
    path('logout/', views.logoutPage, name='logout'),
    path('add_product/', views.addProduct, name='addProduct'),
    
    path('shipped/', views.shipped, name='shipped'),
    path('report/', views.report, name='report')
]