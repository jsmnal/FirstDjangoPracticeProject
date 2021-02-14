from django.contrib import admin

from .models import Album, Image


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("album_name",)}


admin.site.register(Album, AlbumAdmin)


class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("image_name",)}


admin.site.register(Image, ImageAdmin)
