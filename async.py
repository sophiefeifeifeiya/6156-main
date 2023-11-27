import httpx
import asyncio

# URLs for the microservices
ADOPTER_SERVICE = "http://localhost:8000/adopters"
PET_SERVICE = "http://localhost:8001/Pets"
# PET_OWNER_SERVICE = "http://localhost:8002/pet-owner"

async def call_service(url, service_name):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"Received response from {service_name}")
        return response.json()

async def main():
    adopter_task = asyncio.create_task(call_service(ADOPTER_SERVICE, "Adopter Service"))
    pet_task = asyncio.create_task(call_service(PET_SERVICE, "Pet Service"))
    # pet_owner_task = asyncio.create_task(call_service(PET_OWNER_SERVICE, "Pet Owner Service"))

    # responses = await asyncio.gather(adopter_task, pet_task, pet_owner_task)
    responses = await asyncio.gather(adopter_task, pet_task)
    # Do something with the responses

asyncio.run(main())
