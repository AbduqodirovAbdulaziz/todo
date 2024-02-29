from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', Tasks.as_view(),name='tasks'),
    path('logaut/', LogoutView.as_view(),name='logaut'),
    path('ochir/<int:pk>/', ochir),
    path('edit/<int:pk>/', edit),
    path('',LoginView.as_view(), name='login'),


]
