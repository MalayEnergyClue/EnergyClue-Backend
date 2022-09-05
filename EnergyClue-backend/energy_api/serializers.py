from rest_framework import serializers
from energy_api import constants as energy_api_constant

from energy_api import validators as energy_api_validator


class GetQuoteSerializers(serializers.Serializer):
    name = serializers.CharField(required=True)
    mobile_no = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    address = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    frequency = serializers.CharField(required=True)

    def validate(self, data):
        is_valid = True

        if is_valid:
            if data.get("name"):
                if not energy_api_validator.validate_name(data.get("first_name")):
                    raise serializers.ValidationError(
                        "enter first name without special character.")

            if data.get("mobile_no"):
                if not energy_api_validator.validate_mobile(data.get("mobile_no")):
                    raise serializers.ValidationError(
                        "enter valid 10 digit mobile number.")

            if data.get("email"):
                if not energy_api_validator.validate_email(data.get("email")):
                    raise serializers.ValidationError("enter valid email.")

            return data


class CustomerDetailsSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    mobile_no = serializers.CharField(required=True)
    whatsapp_no = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    rating = serializers.ChoiceField(
        choices=energy_api_constant.RATING, required=True)
    frequency = serializers.ChoiceField(
        choices=energy_api_constant.FREQUENCY, required=True)
    address = serializers.CharField(required=True)
    solar_capacity = serializers.CharField(required=True)
    customer_no = serializers.CharField(required=True)
    energy_bill_before = serializers.IntegerField(required=True)
    energy_bill_after = serializers.IntegerField(required=True)

    def validate(self, data):
        is_valid = True

        if is_valid:
            if data.get("first_name"):
                if not energy_api_validator.validate_name(data.get("first_name")):
                    raise serializers.ValidationError(
                        "enter first name without special character.")

            if data.get("last_name"):
                if not energy_api_validator.validate_name(data.get("last_name")):
                    raise serializers.ValidationError(
                        "enter last name without special character.")

            if data.get("mobile_no"):
                if not energy_api_validator.validate_mobile(data.get("mobile_no")):
                    raise serializers.ValidationError(
                        "enter valid 10 digit mobile number.")

            if data.get("email"):
                if not energy_api_validator.validate_email(data.get("email")):
                    raise serializers.ValidationError("enter valid email.")

            return data


class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    mobile_no = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    message = serializers.CharField(required=False)

    def validate(self, data):
        is_valid = True

        if is_valid:
            if data.get("first_name"):
                if not energy_api_validator.validate_name(data.get("first_name")):
                    raise serializers.ValidationError(
                        "enter first name without special character.")

            if data.get("last_name"):
                if not energy_api_validator.validate_name(data.get("last_name")):
                    raise serializers.ValidationError(
                        "enter last name without special character.")

            if data.get("mobile_no"):
                if not energy_api_validator.validate_mobile(data.get("mobile_no")):
                    raise serializers.ValidationError(
                        "enter valid 10 digit mobile number.")

            if data.get("email"):
                if not energy_api_validator.validate_email(data.get("email")):
                    raise serializers.ValidationError("enter valid email.")

            return data


class ServiceSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    mobile_no = serializers.CharField(required=True)
    time_period = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    service_type = serializers.CharField(required=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    month = serializers.CharField(required=True)
    message = serializers.CharField(required=False)

    def validate(self, data):
        is_valid = True

        if is_valid:
            if data.get("first_name"):
                if not energy_api_validator.validate_name(data.get("first_name")):
                    raise serializers.ValidationError(
                        "enter first name without special character.")

            if data.get("last_name"):
                if not energy_api_validator.validate_name(data.get("last_name")):
                    raise serializers.ValidationError(
                        "enter last name without special character.")

            if data.get("mobile_no"):
                if not energy_api_validator.validate_mobile(data.get("mobile_no")):
                    raise serializers.ValidationError(
                        "enter valid 10 digit mobile number.")

            if data.get("email"):
                if not energy_api_validator.validate_email(data.get("email")):
                    raise serializers.ValidationError("enter valid email.")

            return data


class SiteSurveySerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    mobile_no = serializers.CharField(required=True)
    whatsapp_no = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    rating = serializers.ChoiceField(
        choices=energy_api_constant.RATING, required=True)
    frequency = serializers.ChoiceField(
        choices=energy_api_constant.FREQUENCY, required=True)
    address = serializers.CharField(required=True)
    solar_capacity = serializers.CharField(required=True)
    customer_no = serializers.CharField(required=True)
    energy_bill_before = serializers.IntegerField(required=True)
    energy_bill_after = serializers.IntegerField(required=True)

    def validate(self, data):
        is_valid = True

        if is_valid:
            if data.get("first_name"):
                if not energy_api_validator.validate_name(data.get("first_name")):
                    raise serializers.ValidationError(
                        "enter first name without special character.")

            if data.get("last_name"):
                if not energy_api_validator.validate_name(data.get("last_name")):
                    raise serializers.ValidationError(
                        "enter last name without special character.")

            if data.get("mobile_no"):
                if not energy_api_validator.validate_mobile(data.get("mobile_no")):
                    raise serializers.ValidationError(
                        "enter valid 10 digit mobile number.")

            if data.get("email"):
                if not energy_api_validator.validate_email(data.get("email")):
                    raise serializers.ValidationError("enter valid email.")

            return data
