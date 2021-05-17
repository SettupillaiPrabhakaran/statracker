from django.urls import path, include
# from mysite.employee_details import views
from .views import all_users,add_user,modify_user,get_user,delete_user
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('get_all_users/',all_users),
    path('add_user/',add_user),
    path('modify_user/<int:pk>/',modify_user),
    path('get_user/<int:pk>/',get_user),
    path('delete_user/<int:pk>/',delete_user),
]
