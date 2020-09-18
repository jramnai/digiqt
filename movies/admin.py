from django.contrib import admin
from movies.models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    search_fields = ("title",)
    list_display = ("id", "title", "release_date")

