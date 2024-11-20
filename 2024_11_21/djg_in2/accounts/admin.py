from django.contrib import admin

# Register your models here.
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display=( 'announcement_title', 'announcement_content', 'announcement_important', 'created_at','updated_at')
    search_fields=('announcement_title', 'announcement_content')
admin.site.register(Announcement, AnnouncementAdmin)