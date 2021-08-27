from book.models import Tour, TravelAgency
from django.contrib import admin
from .models import Profile, TravelAgency, Tour, Booking
# Register your models here.
admin.site.register(TravelAgency)
admin.site.register(Tour)
admin.site.register(Profile)
admin.site.register(Booking)