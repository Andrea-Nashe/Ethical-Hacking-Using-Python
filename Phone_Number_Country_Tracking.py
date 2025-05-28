import phonenumbers
from phonenumbers import geocoder

# This script uses the phonenumbers library to parse phone numbers and retrieve their country descriptions.
# Make sure to install the phonenumbers library if you haven't already: "pip install phonenumbers"
# Example phone numbers for testing
#Replace these with actual phone numbers you want to check
phoneNumber_1 = phonenumbers.parse("+27123456789")  # Example South African number
phoneNumber_2 = phonenumbers.parse("+447123456789")  # Example UK number

print(geocoder.description_for_number(phoneNumber_1, "en"))
print(geocoder.description_for_number(phoneNumber_2, "en"))