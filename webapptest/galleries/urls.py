from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("albums/", views.albums, name="albums"),
    path("albums/newalbum/", views.AddNewAlbum.as_view(), name="add_album"),
    path("albums/<slug:album_name>/", views.album, name="album"),
    path(
        "albums/<slug:album_name>/new/", views.AddNewImage.as_view(), name="add_image"
    ),
    path("albums/<slug:album_name>/<slug:image_name>/", views.image, name="image"),
    path(
        "albums/<slug:album_name>/<slug:slug>/delete",
        views.DeleteImages.as_view(),
        name="delete_image",
    ),
]
