from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Topic, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        read_only_fields = ('date_added',)
    
        def validate_topic(self,value):
            user = self.context['request'].user
            if value.user != user:
                raise serializers.ValidationError("You can only select topics that belong to you.")
            return value
    

class TopicSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True, read_only=True) #serialize related entries for a particular topic
    class Meta:
        model = Topic
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)