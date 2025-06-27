from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_DEEPSEEK = "api_key"

clients = RyzenthApiClient(
    tools_name=["deepseek"],
    api_key={"deepseek": [{"Authorization": f"Bearer {API_KEY_DEEPSEEK}"}]},
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
        tool="deepseek",
        path="/chat/completions",
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": "hello world!"}
            ],
            "temperature": 0.7
        },
        use_type=ResponseType.JSON
    )
    print(resp)
