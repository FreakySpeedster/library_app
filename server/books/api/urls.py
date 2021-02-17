from .views import bookAPIView
from django.conf.urls import url
from django.urls import path

urlpatterns = [
  path('', bookAPIView.as_view(), name='book-create'),
]