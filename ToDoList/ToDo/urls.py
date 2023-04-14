from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('del/<int:pk>', views.del_ToDo, name='delete'),
]