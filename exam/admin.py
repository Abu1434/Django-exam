from django.contrib import admin

from exam.models import OneModel, TwoModel, SpecialModel, PersonModel

admin.site.register(OneModel)

admin.site.register(TwoModel)

admin.site.register(PersonModel)


@admin.register(SpecialModel)
class SpecialModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name', 'age']
    list_filter = ['name', 'age']
