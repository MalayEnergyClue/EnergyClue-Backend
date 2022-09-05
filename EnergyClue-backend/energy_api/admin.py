from django.contrib import admin
from energy_api import models as energy_api_models

# Register your models here.


@admin.register(energy_api_models.CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",
                    "mobile_no", "email", "created_at")


@admin.register(energy_api_models.Testinomial)
class TestinomialAdmin(admin.ModelAdmin):
    list_display = ("message", "created_at")


@admin.register(energy_api_models.GetQuote)
class GetQuoteAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile_no", "created_at")
    
admin.site.register(energy_api_models.Contact)
admin.site.register(energy_api_models.ServicePage)
admin.site.register(energy_api_models.SiteSurvey)
admin.site.register(energy_api_models.FaqPage)