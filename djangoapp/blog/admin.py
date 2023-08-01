from django.contrib import admin
from .models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug')
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ('name',)
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug')
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ('name',)
    }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published',)
    list_editable = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug')
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ('title',)
    }


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title', 'is_published', 'created_by',)
    list_editable = ('is_published',)
    list_display_links = ('title',)
    list_filter = ('category', 'is_published')
    search_fields = ('id', 'title', 'slug', 'excerpt', 'content',)
    list_per_page = 50
    ordering = ('-id',)
    readonly_fields = ('created_at', 'created_by', 'update_at', 'update_by')
    prepopulated_fields = {
        "slug": ('title',)
    }

    def save_model(self, request, obj, form, change) -> None:
        if change:
            obj.update_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
