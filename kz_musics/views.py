from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from . models import Songs,Artist,Genre


# Create your views here.

class GenreV:

    def get_genres(self):
        return Genre.objects.all()

class SongsView(GenreV, ListView):

    model = Songs

class SongDetailView(DetailView):

    model = Songs
    slug_field = "url"

class ArtistsView(ListView):

    model = Artist

class ArtistDetailView(View):

    def get(self, request, pk):
        artist = Artist.objects.get(id=pk)
        return render(request, "kz_musics/artist_detail.html", {"artist": artist})

class FilterSongsView(GenreV, ListView):

    def get_queryset(self):
        queryset = Songs.objects.filter(genres__in = self.request.GET.getlist("genre"))
        return queryset