from django.urls import path
from port import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('detail/', views.AboutView.as_view(), name='about'),
]