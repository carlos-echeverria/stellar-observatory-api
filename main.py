# aiohttpdemo_client/main.py
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://httpbin.org/get') as resp:
        print(resp.status)
        print(await resp.text())

