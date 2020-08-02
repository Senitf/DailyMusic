from django.urls import path
from .views import MusicList, MusicDelete, MusicDetail, MusicUpdate, MusicCreate, MusicLike, MusicFavorite

app_name = "music"
urlpatterns = [
    path("create/", MusicCreate.as_view(), name="create"),
    path("delete/<int:pk>/", MusicDelete.as_view(), name="delete"),
    path("update/<int:pk>/", MusicUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", MusicDetail.as_view(), name="detail"),
    path("like/<int:music_id>/", MusicLike.as_view(), name='like'),
    path("favorite/<int:music_id>/", MusicFavorite.as_view(), name='favorite'),
    path("", MusicList.as_view(), name="index"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
