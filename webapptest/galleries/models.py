from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


# luodaan Albumeja varten tietokantataulu
class Album(models.Model):
    album_name = models.CharField(_("name"), max_length=100)
    pub_date = models.DateTimeField(_("date"), auto_now_add=True)
    slug = models.SlugField(max_length=100, null=True)

    def __str__(self):
        return self.album_name

    def get_latest_image(self):
        return self.image_set.order_by("-pub_date").first()

    # ylikirjoitetaan save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.album_name)
        super().save(*args, **kwargs)


# luodaan kuvia varten tietokantataulu
class Image(models.Model):
    album = models.ForeignKey(
        Album, verbose_name=_("album"), on_delete=models.SET_NULL, null=True
    )
    image_name = models.CharField(_("name"), max_length=100)
    image_description = models.CharField(_("description"), max_length=400)
    image = models.ImageField(_("image"), upload_to="images/")
    pub_date = models.DateTimeField(_("date"), auto_now_add=True)
    slug = models.SlugField(max_length=100, null=True)

    def __str__(self):
        return f"{self.album}/{self.image_name}"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Image, self).delete(*args, **kwargs)
