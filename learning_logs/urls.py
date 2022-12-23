from django.urls import path
from . import views 


app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
     #Show all topics.
    path('topics/', views.topics, name='topics'),
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]