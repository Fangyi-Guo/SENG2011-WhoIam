from django.contrib import admin

# Register your models here.

from .models import Blood,Reservation,Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('blood', 'bookDate', 'userBooked')
    list_filter = ['bookDate', 'userBooked']
    search_fields = ['bookDate']

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('rsvId', 'bloodType', 'rsvVolume', 'rsvDate', 'userReserved')
    list_filter = ['rsvDate', 'userReserved']
    search_fields = ['rsvDate']

'''class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']'''

    
admin.site.register(Blood)
admin.site.register(Reservation, Book)
#admin.site.register(Cluster, ClusterAdmin)