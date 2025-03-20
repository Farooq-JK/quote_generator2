# admin.py
from django.contrib import admin
from .models import Quote, QuoteItem

class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 1

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client_name', 'date_created')
    inlines = [QuoteItemInline]

admin.site.register(Quote, QuoteAdmin)
