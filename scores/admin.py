from django.contrib import admin

from .models import MusicScore

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields= ('title',)

admin.site.register(MusicScore)