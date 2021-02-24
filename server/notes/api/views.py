from rest_framework import generics, mixins
from notes.models import Note
from .serializers import  noteSerializer
class noteAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'notes'
  serializer_class = noteSerializer
  def get_queryset(self):
    return Note.objects.all()
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)