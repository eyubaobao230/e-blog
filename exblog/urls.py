from django.urls import path

from exblog import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('share/', views.share, name='share'),
    path('list/', views.list, name='list'),
    path('about/', views.about, name='about'),
    path('info/<int:id>/', views.info, name='info'),
    path('gbook', views.gbook, name='gbook'),

]
