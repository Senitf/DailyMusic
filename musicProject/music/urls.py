from django.urls import path
from .views import *

app_name = "music"
urlpatterns = [
    path("create/music/", MusicCreate.as_view(), name="createMusic"),
    path("delete/<int:pk>/", MusicDelete.as_view(), name="deleteMusic"),
    path("update/<int:pk>/", MusicUpdate.as_view(), name="updateMusic"),
    path("detail/<int:pk>/", MusicDetail.as_view(), name="detailMusic"),
    path("like/<int:music_id>/", MusicLike.as_view(), name='likeMusic'),
    path("favorite/<int:music_id>/", MusicFavorite.as_view(), name='favoriteMusic'),
    path("like/", MusicLikeList.as_view(), name="like_listMusic"),
    path("favorite/", MusicFavoriteList.as_view(), name="favorite_listMusic"),
    path("playlist/", MusicPlayList.as_view(), name="playlist"),
    path("likeplaylist/<int:playlist_id>/", PlayListLike.as_view(), name ="likeplaylist"),
    path("create/playlist/", PlayListCreate.as_view(), name="createPlaylist"),
    path("list/music/", MusicList.as_view(), name="listMusic"),
    path("", MusicIndex.as_view(), name="index"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
