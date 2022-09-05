PINCODE_PATTERN = r"\d{4}|\d{6}"
EMAIL_PATTERN = r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
MOBILE_PATTERN = "(0/91)?[6-9][0-9]{9}"


DEMO_ONE = "Demo One"
DEMO_TWO = "Demo Two"
DEMO_THREE = "Demo Three"

SERVICE_TYPE = (
    (DEMO_ONE, DEMO_ONE),
    (DEMO_TWO, DEMO_TWO),
    (DEMO_THREE, DEMO_THREE)
)


RATING = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

INDUSTRIAL = "Industrial"
RESIDENTIAL = "Residential"

PROPERTY_TYPE = (
    (INDUSTRIAL,INDUSTRIAL),
    (RESIDENTIAL,RESIDENTIAL),
)



FREQUENCY = (
    ("15", "15"),
    ("30", "30"),
    ("45", "45"),
    ("60", "60"),
)