from django.test import TestCase

from kz_musics.models import Artist


class ArtistModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Artist.objects.create(name='Yero', age='43', description='dsdsfsdfsf')

    def test_name_label(self):
        artist = Artist.objects.get(id=1)
        field_label = artist._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_first_name_max_length(self):
        artist = Artist.objects.get(id=1)
        max_length = artist._meta.get_field('name').max_length
        self.assertEquals(max_length, 10)

    def test_get_absolute_url(self):
        author = Artist.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/1/')