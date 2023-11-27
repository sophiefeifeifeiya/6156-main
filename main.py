from fastapi import FastAPI
import httpx
import asyncio
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


ADOPTER_SERVICE = "http://52.90.231.152/"
PET_SERVICE = "http://52.0.17.143:8012/"
PET_OWNER_SERVICE = "http://54.92.182.247:8012/"


app = FastAPI()

async def fetch_data(client, url, service_name):
    response = await client.get(url)
    logger.info(f"Received response from {service_name} Service")
    return response.json()

@app.get("/aggregate/sync")
def aggregate_sync():
    with httpx.Client() as client:
        adopter_data = client.get(ADOPTER_SERVICE).json()
        logger.info("Received response from Adopter Service")

        pet_data = client.get(PET_SERVICE).json()
        logger.info("Received response from Pet Service")

        pet_owner_data = client.get(PET_OWNER_SERVICE).json()
        logger.info("Received response from Pet Owner Service")
    
    return {
        "adopter": adopter_data,
        "pet": pet_data,
        "pet_owner": pet_owner_data
    }



@app.get("/aggregate/async")
async def aggregate_async():
    async with httpx.AsyncClient() as client:
        results = []
        for _ in range(10):
            tasks = [
                fetch_data(client, ADOPTER_SERVICE, "Adopter"),
                fetch_data(client, PET_SERVICE, "Pet"),
                fetch_data(client, PET_OWNER_SERVICE, "Pet Owner")
            ]
            random.shuffle(tasks)  # Randomize the order of service calls
            results.append(await asyncio.gather(*tasks))

        return results

