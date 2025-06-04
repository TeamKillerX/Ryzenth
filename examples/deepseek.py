from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

ryz = ApiKeyFrom(..., is_ok=True)

async def main():
    response = await ryz.aio.what.think(
        QueryParameter(
            query="What your name?"
        )
    )
    print(response)
