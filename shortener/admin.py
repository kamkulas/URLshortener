from django.contrib import admin
from .models import URL


class URLAdmin(admin.ModelAdmin):
    """
    Model specifying the way of displaying URL items in admin interface.
    """

    list_display = ('id', 'original_path', 'shortcut')


admin.site.register(URL, URLAdmin)
