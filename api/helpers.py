import aiohttp, asyncio
from projectservice.settings import *


# Helpers

async def fecth(session, url):
    async with session.get(url) as response:
        resp = await response.json()
        return resp


async def fetch_all(cities):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for city in cities:
            tasks.append(
                fecth(
                    session,
                    API_BASE_URL % (city, API_KEY),
                )
            )
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return responses


def get_cities():
    f = open(PATH_FILE, 'r')
    parsed_file = f.read().split(',')
    cities = [num.strip() for num in parsed_file]

    return cities