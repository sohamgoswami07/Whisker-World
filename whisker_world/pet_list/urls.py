from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)