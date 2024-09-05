import asyncio 
import discord 
from discord import Webhook
import aiohttp 

async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title="This is from a webhook!")
        await webhook.send(embed=embed, username="Richard Web")
        
if __name__ == "__main__":
    url = "https://discord.com/api/webhooks/1280236549912662127/Kdru2e8zgfpNvA-mzRPUPyiN7WK_Ng4m0mOPxekEeke_AJaBtdDuFvkZ6I9A2UsRfqHR"

    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close()