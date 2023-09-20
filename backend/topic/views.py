from django.contrib.auth import get_user_model #serves same as User i.e (from django.contrib.auth import User)
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .serializers import TopicSerializer, EntrySerializer,  UserSerializer
from .models import Topic, Entry


class TopicListCreateView(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    def get_queryset(self):
        user = self.request.user
        # user can only view, create own Topics
        return Topic.objects.filter(user=user)
    
    def perform_create(self, serializer):
        #create for the authenticated user not superuser
        serializer.save(user=self.request.user)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own Topics
        return Topic.objects.filter(user=user)


class EntryListCreateView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    Permission_classes = (IsAuthorOrReadOnly,)
    def get_queryset(self):
        user = self.request.user
        topic_id = self.kwargs['topic_id']
        # user can only view, create own entries
        return Entry.objects.filter(topic__id=topic_id, topic__user=user)
    
    
class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntrySerializer
    Permission_classes = (IsAuthorOrReadOnly,)
    def get_queryset(self):
        user = self.request.user
        topic_id = self.kwargs['topic_id']
        # user can only update, delete own entries
        return Entry.objects.filter(topic__id=topic_id, topic__user=user)


class UserListCreateView(generics.ListCreateAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer