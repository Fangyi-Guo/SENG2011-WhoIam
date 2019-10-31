from django.contrib import admin

# Register your models here.

from .models import Blood,Reservation,Book

class BloodAdmin(admin.ModelAdmin):
    model = Blood
    list_display = ('bloodtype', 'volume', 'expdate', 'isTested')
    list_filter = ['bloodtype', 'expdate']
    search_fields = ['expdate']

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('blood', 'bookDate', 'userBooked')
    list_filter = ['bookDate', 'userBooked']
    search_fields = ['bookDate']

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('bloodType', 'rsvVolume', 'rsvDate', 'userReserved')
    list_filter = ['rsvDate', 'userReserved']
    search_fields = ['rsvDate']

'''class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']'''

    
admin.site.register(Blood,BloodAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Book,BookAdmin)
#admin.site.register(Cluster, ClusterAdmin)