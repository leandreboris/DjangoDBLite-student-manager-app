from django.conf.urls import url
from StudentsApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  

    url(r'^students/$', views.studentApi),
    url(r'^students/([0-9]+)$', views.studentApi),
    url(r'^savePicture/$', views.savePicture)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)