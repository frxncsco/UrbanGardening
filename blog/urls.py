from django.urls import path
from . import views 

urlpatterns = [     
    path('', views.startseite, name='startseite'),     
    path('post/<int:pk>/', views.post_detail, name='post_detail'),     
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('events', views.events, name='events'), #EVENT
    path('event/new/', views.event_new, name='event_new'), #EVENT
    #path('urbangardening', views.urbangardening, name='urbangardening'),
    path('uebermich', views.ubermich, name='ubermich'),
    path('blog', views.post_list, name='post_list'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),#EVENT
    path('event/<int:pk>/', views.event_detail, name='event_detail'), #EVENT
]