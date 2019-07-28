from django.contrib import admin
from .models import Comers, Status

# Register your models here.


@admin.register(Status)
class AttendAdmin(admin.ModelAdmin):
    list_display = ('attend_name', 'status_time')


@admin.register(Comers)
class AttendAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'pub_date')