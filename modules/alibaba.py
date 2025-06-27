from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_ALIBABA = "api_key"

clients = RyzenthApiClient(
    tools_name=["alibaba"],
    api_key={
        "alibaba": [
            {"Authorization": f"Bearer {API_KEY_ALIBABA}"}
        ]
    },
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
    clients = await clients.post(
        tool="alibaba",
        path="/chat/completions",
        json={
            "model": "qwen-plus",
            "messages": [
                {"role": "user", "content": "hello world!"}
            ],
            "temperature": 0.7
        },
        use_type=ResponseType.JSON
    )
