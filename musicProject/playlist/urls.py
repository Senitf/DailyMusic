from django.urls import path
from .views import *

app_name = "playlist"
urlpatterns = [
    path("list/", List.as_view(), name="list"),
    path("like/<int:playlist_id>/", Like.as_view(), name ="like"),
    path("create/", Create.as_view(), name="create"),
    path("detail/<int:pk>/", Detail.as_view(), name="detail"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
