from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

ryz = ApiKeyFrom("your-api-key-v1")

async def main():
    image_data = await ryz.aio.images.generate(
        QueryParameter(query="make logo telegram blue")
    )
    with open("image.jpg", "wb") as f:
        f.write(image_data)
    print("Saved file: image.jpg")

def something_main():
    image_data = ryz._sync.images.generate(
        QueryParameter(query="make logo telegram red")
    )
    with open("image.jpg", "wb") as f:
        f.write(image_data)
    print("Saved file: image.jpg")
