from .views import noteAPIView
from django.conf.urls import url
from django.urls import path

urlpatterns = [
  path('', noteAPIView.as_view(), name='note-create'),
]