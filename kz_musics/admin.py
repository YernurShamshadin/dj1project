from django.contrib import admin
from .models import Category, Artist, Songs, Genre, Author

# Register your models here.
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Songs)
admin.site.register(Genre)
admin.site.register(Author)