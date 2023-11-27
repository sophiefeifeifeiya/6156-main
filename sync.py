import requests

# URLs for the microservices
ADOPTER_SERVICE = "http://54.90.105.146/adopters"
PET_SERVICE = "http://localhost:8001/Pets"
# PET_OWNER_SERVICE = "http://localhost:8002/pet-owner"

def call_service(url, service_name):
    response = requests.get(url)
    print(f"Received response from {service_name}")
    return response.json()

def main():
    adopter_data = call_service(ADOPTER_SERVICE, "Adopter Service")
    pet_data = call_service(PET_SERVICE, "Pet Service")
    # pet_owner_data = call_service(PET_OWNER_SERVICE, "Pet Owner Service")
    # Do something with the data

main()
