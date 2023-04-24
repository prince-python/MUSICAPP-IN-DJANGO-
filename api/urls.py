from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .api import *
urlpatterns = [
    path('song/', SongViewSet.as_view()),
    path('songshow/', SongShowViewSet.as_view()),
    path('songupdate/<int:pk>/', SongUpdateViewSet.as_view()),
    path('songdelete/<int:pk>/', SongDeleteViewSet.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)