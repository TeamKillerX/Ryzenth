import asyncio

from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_PAXSENIX = "api_key"

clients = RyzenthApiClient(
    tools_name=["paxsenix"],
    api_key={"paxsenix": [{"Authorization": f"Bearer {API_KEY_PAXSENIX}"}]},
    rate_limit=20,
    use_default_headers=True,
    settings={
        "logging": [
            {"level": "INFO"},
            {"httpx_log": False}
        ]
    }
)

async def main():
    resp = await clients.post(
        tool="paxsenix",
        path="/v1/chat/completions",
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": "hello world!"}
            ]
        },
        use_type=ResponseType.JSON
    )
    print(resp)

if __name__ == "__main__":
    asyncio.run(main())
