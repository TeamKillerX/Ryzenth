import asyncio
from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType
from Ryzenth.helper._images import ResponseFileImage

RYZENTH_API_KEY = "api_key"

clients = RyzenthApiClient(
    tools_name=["ryzenth"],
    api_key={"ryzenth": [{"x-api-key": RYZENTH_API_KEY}]},
    use_default_headers=True,
    use_httpx=True,
    settings={
        "logging": [
            {"level": "INFO"},
            {"httpx_log": False}
        ]
    }
)

async def main():
    generate_resp = await ResponseFileImage(
        response_content=await clients.get(
            tool="ryzenth",
            path="/api/v1/flux/black-forest-labs/flux-1-schnell",
            params={"query": "bikin logo GTA"},
            use_type=ResponseType.JSON
        )
    ).to_save(file_path="pro.jpg")

if __name__ == "__main__":
    asyncio.run(main())
