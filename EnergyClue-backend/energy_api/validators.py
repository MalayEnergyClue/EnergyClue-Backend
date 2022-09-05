from re import compile
from energy_api import constants as energy_api_constant

def validate_name(name):
    return (
        compile(r"^[a-zA-Z ]+(?: [a-zA-Z]+){0,2}$").match(name)
    )
    
def validate_mobile(mobile):
    return True if compile(energy_api_constant.MOBILE_PATTERN).match(mobile) else False

def validate_email(email):
    return True if compile(energy_api_constant.EMAIL_PATTERN).match(email) else False