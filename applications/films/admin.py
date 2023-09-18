from django.contrib import admin

from applications.films.models import Films, Comment, FilmImage


class ImageInLineAdmin(admin.TabularInline):
    model = FilmImage
    fields = ('image',)
    max_num = 5

@admin.register(Films)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    list_filter = ['owner']
    list_fields = ['title']

    def like_count(self, obj):
        return obj.likes.filter(is_like=True).count()

admin.site.register(Comment)

