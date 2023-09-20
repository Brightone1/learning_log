from django.urls import path
from .views import TopicListCreateView, TopicDetail, EntryListCreateView, EntryDetail, UserListCreateView, UserDetail

app_name = 'topic'

urlpatterns = [
    path('users/', UserListCreateView.as_view()), 
    path('users/<int:pk>/', UserDetail.as_view()),

    path('topics/', TopicListCreateView.as_view()),
    path('topics/<int:pk>/', TopicDetail.as_view()),

    path('topics/<int:topic_id>/entries/', EntryListCreateView.as_view()),
    path('topics/<int:topic_id>/entries/<int:pk>/', EntryDetail.as_view()),
]
