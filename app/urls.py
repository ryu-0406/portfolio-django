from django.urls import path, include
from app import views
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib import admin

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]