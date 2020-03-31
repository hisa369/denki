from django.contrib import admin

from .models import Location, WeatherData


class PostAdmin(admin.ModelAdmin):
    list_display = ('location', 'nengetu', 'kuchou', 'dentou', 'goukei')
    ordering = ('-nengetu',)


admin.site.register(Location)
admin.site.register(WeatherData, PostAdmin)
