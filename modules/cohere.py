from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

API_KEY_COHERE = "api_key"

clients = RyzenthApiClient(
    tools_name=["cohere"],
    api_key={"cohere": [{"Authorization": f"Bearer {API_KEY_COHERE}"}]},
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
        tool="cohere",
        path="/chat",
        json={
            "chat_history": [],
            "message": "What year was he born?",
            "connectors": [{"id": "web-search"}]
        },
        use_type=ResponseType.JSON
    )
    print(resp)
