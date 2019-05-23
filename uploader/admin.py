from django.contrib import admin

from .models import Upload


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'pic', 'upload_date')
    list_filter = ('expired_date','pic')

    fieldsets = (
        (None, {
            'fields': ('pic', 'upload_date',)
        }),
        ('Availability', {
            'fields': ('expired_date', 'borrower')
        }),
    )
