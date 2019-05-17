from django.contrib import admin
from .models import History

# Register your models here.


@admin.register(History)
class HistoryInline(admin.ModelAdmin):
    list_display = ('url', 'created')
    list_filter = ('created', )