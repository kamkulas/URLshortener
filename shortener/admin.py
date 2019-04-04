from django.contrib import admin
from .models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_path', 'shortcut')


admin.site.register(URL, URLAdmin)
