import asyncio
from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_GROK = "api_key"

clients = RyzenthApiClient(
    tools_name=["grok"],
    api_key={"grok": [{"Authorization": f"Bearer {API_KEY_GROK}"}]},
    rate_limit=20,
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
    resp = await clients.post(
        tool="grok",
        path="/chat/completions",
        json={
            "model": "grok-3",
            "messages": [
                {"role": "user", "content": "hello world!"}
            ],
            "temperature": 0.7
        },
        use_type=ResponseType.JSON
    )
    print(resp)

if __name__ == "__main__":
    asyncio.run(main())
