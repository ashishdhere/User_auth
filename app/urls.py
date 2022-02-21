from django.urls import path
from app import views

urlpatterns = [
    path('',views.register),
    path('login/',views.login,name="login"),
    path('data/',views.data,name='data'),

]
