from django.contrib import admin
from .models import Booking, Driver, Vehicle
from school.models import Class, Student

admin.site.register(Driver)
admin.site.register(Vehicle)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	fields = ('teacher', 'subject', ('class_involved', 'no_of_people'), 'purpose', 'destination', ('trip_date', 'departure_time'), ('transport_back', 'approx_time_back'), ('approved', 'approved_by'), ('vehicle', 'driver'), 'students')
	list_display = ('subject', 'class_involved', 'trip_date', 'destination', 'approved_by')
	list_filter = ('teacher', 'subject', 'trip_date', 'date_created', 'approved')
	ordering = ('-trip_date',)
	search_fields = ('subject', 'trip_date', 'destination')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
	ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	fields = ('class_number', ('first_name', 'last_name'), 'class_name')
	list_display = ('class_number', 'first_name', 'last_name', 'class_name')
	list_filter = ('class_name',)
	search_fields = ('class_number', 'first_name', 'last_name', 'class_name')

# Name = Admin, Pass = Transport5