from Ryzenth import ApiKeyFrom
from Ryzenth._errors import ParamsRequiredError

ryz = ApiKeyFrom("api-key-v1")


async def main():
    try:
        response = await ryz.aio.fonts.scanning(text="𝖍𝖊𝖑𝖑𝖔 𝖘𝖎𝖒𝖇𝖔𝖑")
        print(response)
    except ParamsRequiredError:
        print("Parameter teks wajib diisi!")
