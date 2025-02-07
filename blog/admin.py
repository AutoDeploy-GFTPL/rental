from django.contrib import admin
from.models import *

@admin.register(BlogCategory)
class CategoryDisplay(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )
    
@admin.register(Tags)
class TagsDisplay(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(Blog)
class BlogDisplay(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'date', )
    
