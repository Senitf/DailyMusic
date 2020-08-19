from django.urls import path
from .views import *

app_name = "music"
urlpatterns = [
    path("create/", Create.as_view(), name="create"),
    path("delete/<int:pk>/", Delete.as_view(), name="delete"),
    path("update/<int:pk>/", Update.as_view(), name="update"),
    path("detail/<int:pk>/", Detail.as_view(), name="detail"),
    path("like/<int:music_id>/", Like.as_view(), name='like'),
    path("favorite/<int:music_id>/", Favorite.as_view(), name='favorite'),
    path("likelist/", Likelist.as_view(), name="likelist"),
    path("favoritelist/", Favoritelist.as_view(), name="favoritelist"),
    path("list/", List.as_view(), name="list"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
