from Ryzenth import ApiKeyFrom
from Ryzenth._errors import ErrorParamsRequired

ryz = ApiKeyFrom("api-key-v1")

async def main():
    try:
        response = await ryz.aio.fonts.scanning(text="𝖍𝖊𝖑𝖑𝖔 𝖘𝖎𝖒𝖇𝖔𝖑")
        print(response)
    except ErrorParamsRequired:
        print("Parameter teks wajib diisi!")
