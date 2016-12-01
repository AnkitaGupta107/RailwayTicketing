from django.contrib import admin
from .models import City, Train, BookedTicket
# Register your models here.

admin.site.register(City)
admin.site.register(Train)
admin.site.register(BookedTicket)
