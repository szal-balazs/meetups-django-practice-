from django.contrib import admin

from .models import Meetup, Location, Participant, Organizer

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    list_filet = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Organizer)
