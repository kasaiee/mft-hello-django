from django.contrib import admin
from app_1.models import Post


@admin.action(description="published")
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.action(description="unpublished")
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('is_published', )
    list_display = ('title', 'is_published', )
    list_editable = ('is_published', )
    actions = [make_published, make_unpublished]



admin.site.register(Post, PostAdmin)