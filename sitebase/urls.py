from django.urls import path

from . import views

app_name = 'sitebase'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.news, name='news'),
    path('news/<int:topic_id>/', views.newsdetail, name='newsdetail'),
]
