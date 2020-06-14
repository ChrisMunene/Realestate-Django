from django.contrib import admin
from .models import Inquiry

# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing_name', 'email', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'listing_name')
    list_per_page = 25

admin.site.register(Inquiry, InquiryAdmin)
