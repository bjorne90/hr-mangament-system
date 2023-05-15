from django.urls import path
from . import views
from .views import links

app_name = 'profiles'

urlpatterns = [
    path('detail/', views.profile_detail, name='profile_detail'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('work_shifts/', views.work_shifts, name='work_shifts'),
    path('links/', links, name='links'),
    path('employees/', views.employees, name='employees'),
]
