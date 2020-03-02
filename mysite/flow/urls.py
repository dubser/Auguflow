from django.urls import path

from . import views

urlpatterns = [
    path('exec', views.exec, name='exec'),
    path('', views.test, name='test'),
]

