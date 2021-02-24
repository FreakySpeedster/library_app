from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from notes.models import Note

class noteSerializer(TaggitSerializer, serializers.ModelSerializer):
  labels = TagListSerializerField()

  class Meta:
    model = Note
    fields = (
      'id',
      'title',
      'topic',
      'content',
      'labels'
    )