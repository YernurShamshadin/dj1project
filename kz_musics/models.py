from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    '''Категории'''
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Artist(models.Model):
    '''Артисты'''
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="artists/", null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("artist_details", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"


class Genre(models.Model):
    '''Жанры'''
    name = models.CharField("Жанр", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Songs(models.Model):
    '''Песни'''
    title = models.CharField("Названия",max_length=150)
    year = models.PositiveSmallIntegerField("Дата выхода")
    lyrics = models.TextField("Текст песни")
    artist = models.ManyToManyField(Artist, verbose_name = "артисты", related_name="song_artist")
    category = models.ForeignKey(Category, verbose_name="", on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("song_details", kwargs={'slug': self.url })

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class Author(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField()
