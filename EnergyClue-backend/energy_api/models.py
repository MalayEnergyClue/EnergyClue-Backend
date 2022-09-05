from django.db import models

from energy_api import constants as energy_api_constant
# Create your models here.

class FaqPage(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def get_details(self):
        return {
            "question" :self.question,
            "answer":self.answer
        }
class GetQuote(models.Model):
    """
        Get Quote Model
    """
    # full name
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=500)
    date = models.DateField(null=True, blank=True)
    frequency = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ServicePage(models.Model):
    """
        Service Page Model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    mobile_no = models.CharField(max_length=50)
    time_period = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    service_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    month = models.CharField(max_length=100)
    message = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Contact(models.Model):
    """
        Contact Model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=500)

class CustomerDetails(models.Model):
    """
        Customer Details Model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    whatsapp_no = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    rating = models.CharField(choices=energy_api_constant.RATING, max_length=50)
    frequency = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    solar_capacity = models.CharField(max_length=100)
    customer_no = models.CharField(max_length=50)
    energy_bill_before = models.IntegerField()
    energy_bill_after = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class SiteSurvey(models.Model):
    """
        Site Survey Model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    whatsapp_no = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    frequency = models.CharField(max_length=100)
    rating = models.CharField(choices=energy_api_constant.RATING, max_length=50)
    address = models.CharField(max_length=500)
    solar_capacity = models.CharField(max_length=100)
    customer_no = models.CharField(max_length=50)
    energy_bill_before = models.IntegerField()
    energy_bill_after = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Testinomial(models.Model):
    """
        Testinomial Model
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    business_name = models.CharField(max_length=500)
    rating = models.CharField(choices=energy_api_constant.RATING, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def get_details(self):
        return {
            "name" : self.name,
            "email" : self.email,
            "message" : self.message,
            "business_name" : self.business_name,
            "rating" : self.rating,
        }
