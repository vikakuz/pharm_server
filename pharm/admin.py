from django.contrib import admin

from .models import PharmacyConditions, DrugForm, PharmacotherapeuticGroup, Pharmacokinetics, Manual, IndicationsForUse


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ['value']


class PharmacokineticsAdmin(admin.ModelAdmin):
    list_display = ('common_information', 'absorption', 'distribution', 'metabolism', 'breeding')


class IndicationsForUseAdmin(admin.ModelAdmin):
    list_display = (
        'common_information', 'for_children', 'for_elderly_people', 'for_pregnant_women', 'for_lactating_mothers')


class ManualAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'name')
    # search_fields = ['name']


admin.site.register(PharmacyConditions, DictionaryAdmin)
admin.site.register(PharmacotherapeuticGroup, DictionaryAdmin)
admin.site.register(DrugForm, DictionaryAdmin)

admin.site.register(Pharmacokinetics, PharmacokineticsAdmin)
admin.site.register(IndicationsForUse, IndicationsForUseAdmin)
admin.site.register(Manual, ManualAdmin)
