from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("likes",views.likes,name="likes"),
    #API
    path("like",views.like,name="like"),] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)