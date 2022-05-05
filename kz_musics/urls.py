from django.urls import path
from . import views


urlpatterns = [
    path("", views.SongsView.as_view()),
    path("artists/", views.ArtistsView.as_view()),
    path("filter/", views.FilterSongsView.as_view(),name = 'filter'),
    path("<int:pk>/", views.ArtistDetailView.as_view(), name='artist_details'),
    path("<slug:slug>/", views.SongDetailView.as_view(), name='song_details'),

]