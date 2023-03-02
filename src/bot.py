import aiohttp

DEBUG_TOKEN_API_TELEGRAM = "5205378717:AAHVutFHCDnZlqBInfaz5GJXBlsDaRkStfI"
DEBUG_CHAT_ID = "899093886"

async def send_to_channel(message):
    chunk_length = 4096
    chunks = [message[i:i+chunk_length] for i in range(0, len(message), chunk_length)]

    for chunk_message in chunks:
        url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(
            DEBUG_TOKEN_API_TELEGRAM, DEBUG_CHAT_ID, chunk_message)
        
        async with aiohttp.ClientSession() as session:
            await session.post(url)