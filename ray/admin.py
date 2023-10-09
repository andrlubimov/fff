from django.contrib import admin

from ray.models import uslugi


# Register your models here.


class UslugiAdmin(admin.ModelAdmin):
    list_display = ('name', "body", "title", 'id',)


admin.site.register(uslugi, UslugiAdmin)
