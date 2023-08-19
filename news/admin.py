from django.contrib import admin

from news.models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "published_time", "status", "category"]
    list_filter = ["status", "created_time", "published_time", "category"]
    date_hierarchy = "published_time"
    search_fields = ["title", "body"]
    ordering = ["status", "published_time"]

@admin.register(Category)
class CateoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]