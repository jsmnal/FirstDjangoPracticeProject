from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Image
from .forms import ImageAddForm, AlbumAddForm, DeleteImages
from django.views.generic import CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from galleries.forms import UserForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# etusivun näkymä
def index(request):
    latest_album_list = Album.objects.order_by("-pub_date")
    latest_image_list = Image.objects.all().order_by("-pub_date")[:4]
    context = {
        "latest_album_list": latest_album_list,
        "latest_image_list": latest_image_list,
    }
    return render(request, "galleries/index.html", context)


# albumit-näkymä
def albums(request):
    latest_album_list = Album.objects.order_by("-pub_date")
    context = {
        "latest_album_list": latest_album_list,
    }
    return render(request, "galleries/albums.html", context)


# kuvien tarkastelu näkymä albumissa
@login_required
def album(request, album_name):
    album = get_object_or_404(Album, slug=album_name)
    return render(request, "galleries/album.html", {"album": album})


@login_required
def image(request, album_name, image_name):
    return HttpResponse(image_name)


# rekisteröitymisnäkymä
def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            print(form.error_messages)

    form = UserForm
    return render(request, "galleries/registration.html", context={"form": form})


def logout_request(request):
    logout(request)
    return redirect("login")


# kirjautumisnäkymä
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "galleries/login.html", {"form": form})


# kuvan lisäys näkymä
class AddNewImage(LoginRequiredMixin, CreateView):
    model = Image
    form_class = ImageAddForm
    template_name = "galleries/newimage.html"

    def get_success_url(self, **kwargs):
        return reverse("album", args=[(self.object.album.slug)])

    # haetaan albumin tiedot
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.get(slug=self.kwargs.get("album_name"))
        return context


# albumin lisäys näkymä
class AddNewAlbum(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumAddForm
    template_name = "galleries/newalbum.html"
    success_url = reverse_lazy("albums")


class DeleteImages(LoginRequiredMixin, DeleteView):
    model = Image
    form_class = DeleteImages
    template_name = "galleries/deleteimage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.get(slug=self.kwargs.get("album_name"))
        return context

    def get_success_url(self, **kwargs):
        return reverse("album", args=[(self.object.album.slug)])
