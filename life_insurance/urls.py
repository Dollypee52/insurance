from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.redirect),
    path('redirect/',views.redirect),
    path('about/',views.about, name='about'),
    path('policy_details/<int:pk>/', views.policy_details, name='policy_details'),
    path('policy_list/', views.policy_list, name='policy_list')
]