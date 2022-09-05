
from energy_api import models as energy_api_model
from energy_api import serializers as energy_api_serializers
from energy_api import utils as energy_api_utils

from rest_framework.views import APIView

from sms import send_sms

from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class TestinomialDetail(APIView):
    
    @staticmethod
    def get(request):
        testinomial_instance = energy_api_model.Testinomial.objects.all()

        return energy_api_utils.create_response(
            data=[testinomial.get_details() for testinomial in testinomial_instance], code=200
        )
        
class GetQuoteDetail(APIView):
    
    @staticmethod
    def post(request):
        serializer_instance = energy_api_serializers.GetQuoteSerializers(data = request.data)
        
        if not serializer_instance.is_valid():
            return energy_api_utils.create_response(serializer_instance.errors, 400)
        
        energy_api_model.GetQuote.objects.create(
            name=serializer_instance.validated_data.get("name"),
            mobile_no=serializer_instance.validated_data.get("mobile_no"),
            email = serializer_instance.validated_data.get("email"),
            address=serializer_instance.validated_data.get("address"),
            date = serializer_instance.validated_data.get("date"),
            frequency=serializer_instance.validated_data.get("frequency"),
            created_at=timezone.localtime(timezone.now()),
        )
        
        send_mail(
            subject="Get Quote Details For N-Energy",
            message="Thanks your Details are Recieved",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[serializer_instance.validated_data.get("email"),],
        )
        return energy_api_utils.create_response(data="Ok", code=200)
    
class CustomerDetail(APIView):
    
    @staticmethod
    def post(request):
        serializer_instance = energy_api_serializers.CustomerDetailsSerializer(data = request.data)
        
        if not serializer_instance.is_valid():
            return energy_api_utils.create_response(serializer_instance.errors, 400)
        
        energy_api_model.CustomerDetails.objects.create(
            first_name=serializer_instance.validated_data.get("first_name"),
            last_name=serializer_instance.validated_data.get("last_name"),
            mobile_no=serializer_instance.validated_data.get("mobile_no"),
            whatsapp_no=serializer_instance.validated_data.get("whatsapp_no"),
            email=serializer_instance.validated_data.get("email"),
            rating = serializer_instance.validated_data.get("rating"),
            frequency = serializer_instance.validated_data.get("frequency"),
            address = serializer_instance.validated_data.get("address"),
            solar_capacity = serializer_instance.validated_data.get("solar_capacity"),
            customer_no = serializer_instance.validated_data.get("customer_no"),
            energy_bill_before = serializer_instance.validated_data.get("energy_bill_before"),
            energy_bill_after = serializer_instance.validated_data.get("energy_bill_after"),
            created_at=timezone.localtime(timezone.now()),
        )
        
        return energy_api_utils.create_response(data="Ok", code=200)
    
class Contact(APIView):
    @staticmethod
    def post(request):
        serializer_instance = energy_api_serializers.ContactSerializer(data = request.data)
        
        if not serializer_instance.is_valid():
            return energy_api_utils.create_response(serializer_instance.errors, 400)
        
        energy_api_model.Contact.objects.create(
            first_name=serializer_instance.validated_data.get("first_name"),
            last_name=serializer_instance.validated_data.get("last_name"),
            mobile_no=serializer_instance.validated_data.get("mobile_no"),
            email=serializer_instance.validated_data.get("email"),
            message = serializer_instance.validated_data.get("message"),
        )
        
        return energy_api_utils.create_response(data="Ok", code=200)
    
class Service(APIView):
    @staticmethod
    def post(request):
        serializer_instance = energy_api_serializers.ServiceSerializer(data = request.data)
        
        if not serializer_instance.is_valid():
            return energy_api_utils.create_response(serializer_instance.errors, 400)
        
        energy_api_model.ServicePage.objects.create(
            first_name=serializer_instance.validated_data.get("first_name"),
            last_name=serializer_instance.validated_data.get("last_name"),
            address = serializer_instance.validated_data.get("address"),
            mobile_no=serializer_instance.validated_data.get("mobile_no"),
            time_period =serializer_instance.validated_data.get("time_period"),
            email=serializer_instance.validated_data.get("email"),
            service_type = serializer_instance.validated_data.get("service_type"),
            start_date = serializer_instance.validated_data.get("start_date"),
            end_date = serializer_instance.validated_data.get("end_date"),
            month = serializer_instance.validated_data.get("month"),
            message = serializer_instance.validated_data.get("message"),
            created_at=timezone.localtime(timezone.now())
        )
        
        send_mail(
            subject="Energy Clue Test Email",
            message="This is Demo Text.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[serializer_instance.validated_data.get("email"),],
        )
        
        return energy_api_utils.create_response(data="Ok", code=200)
    
class SiteSurvey(APIView):
    @staticmethod
    def post(request):
        serializer_instance = energy_api_serializers.SiteSurveySerializer(data = request.data)
        
        if not serializer_instance.is_valid():
            return energy_api_utils.create_response(serializer_instance.errors, 400)
        
        energy_api_model.SiteSurvey.objects.create(
            first_name=serializer_instance.validated_data.get("first_name"),
            last_name=serializer_instance.validated_data.get("last_name"),
            mobile_no=serializer_instance.validated_data.get("mobile_no"),
            whatsapp_no=serializer_instance.validated_data.get("whatsapp_no"),
            email=serializer_instance.validated_data.get("email"),
            rating = serializer_instance.validated_data.get("rating"),
            frequency = serializer_instance.validated_data.get("frequency"),
            address = serializer_instance.validated_data.get("address"),
            solar_capacity = serializer_instance.validated_data.get("solar_capacity"),
            customer_no = serializer_instance.validated_data.get("customer_no"),
            energy_bill_before = serializer_instance.validated_data.get("energy_bill_before"),
            energy_bill_after = serializer_instance.validated_data.get("energy_bill_after"),
            created_at=timezone.localtime(timezone.now()),
        )
        
        return energy_api_utils.create_response(data="Ok", code=200)

class GetFaq(APIView):
    @staticmethod
    def get(request):
        faq_instances = energy_api_model.FaqPage.objects.all()
        return energy_api_utils.create_response(
            data=[
                faq.get_details()
                for faq in faq_instances
            ],
            code=200
        )