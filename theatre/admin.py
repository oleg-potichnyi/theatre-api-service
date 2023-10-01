from django.contrib import admin

from theatre.models import (
    TheatreHall,
    Genre,
    Actor,
    Play,
    Performance,
    Reservation,
    Ticket,
)

admin.site.register(TheatreHall)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(Performance)
admin.site.register(Reservation)
admin.site.register(Ticket)
