from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtors')
    list_display_links = ('id', 'title')
    list_filter = ['realtors']
    list_editable = ['is_published']
    search_fields = ('title', 'description', 'realtors__name', 'address', 'city', 'state', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)