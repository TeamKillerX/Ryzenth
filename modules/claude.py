import asyncio

from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_CLAUDE = "api_key"

clients = RyzenthApiClient(
    tools_name=["claude"],
    api_key={"claude": [{"x-api-key": API_KEY_CLAUDE}]}, # custom header anthropic-version: 2023-06-01
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
        tool="claude",
        path="/messages",
        json={
            "model": "claude-opus-4-20250514",
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
