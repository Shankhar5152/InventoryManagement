from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),    # Homepage view
    path('about/', views.AboutView.as_view(), name='about'),  # About page view
] 