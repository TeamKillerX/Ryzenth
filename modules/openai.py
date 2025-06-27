from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_OPENAI = "api_key"

clients = RyzenthApiClient(
    tools_name=["openai"],
    api_key={
        "openai": [
            {"Authorization": f"Bearer {API_KEY_OPENAI}"}
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
    resp = await clients.post(
        tool="openai",
        path="/chat/completions",
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": "hello world!"}
            ],
            "temperature": 0.7
        },
        use_type=ResponseType.JSON
    )
