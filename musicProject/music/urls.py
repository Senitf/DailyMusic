from django.urls import path
from .views import *

app_name = "music"
urlpatterns = [
    path("create/", MusicCreate.as_view(), name="create"),
    path("delete/<int:pk>/", MusicDelete.as_view(), name="delete"),
    path("update/<int:pk>/", MusicUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", MusicDetail.as_view(), name="detail"),
    path("like/<int:music_id>/", MusicLike.as_view(), name='like'),
    path("favorite/<int:music_id>/", MusicFavorite.as_view(), name='favorite'),
    path("like/", MusicLikeList.as_view(), name="like_list"),
    path("favorite/", MusicFavoriteList.as_view(), name="favorite_list"),
    path("playlist/", MusicPlayList.as_view(), name="playlist"),
    path("likeplaylist/<int:playlist_id>/", PlayListLike.as_view(), name ="likeplaylist"),
    path("", MusicList.as_view(), name="index"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
