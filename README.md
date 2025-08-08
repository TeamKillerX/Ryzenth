# Ryzenth Library
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/Ryzenth)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/Ryzenth/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-GPL-pink)](https://github.com/TeamKillerX/Ryzenth/blob/dev/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Ryzenth - Version](https://img.shields.io/pypi/v/Ryzenth?style=round)](https://pypi.org/project/Ryzenth)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/Ryzenth/dev.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/Ryzenth/dev)

<div align="center">
    <a href="https://pepy.tech/project/Ryzenth"><img src="https://static.pepy.tech/badge/Ryzenth" alt="Downloads"></a>
    <a href="https://github.com/TeamKillerX/Ryzenth/workflows/"><img src="https://github.com/TeamKillerX/Ryzenth/actions/workflows/async-tests.yml/badge.svg" alt="API Tests"/></a>
</div>

---

![Image](https://github.com/user-attachments/assets/ebb42582-4d5d-4f6a-8e8b-78d737810510)

---
**Ryzenth** is this cool Multi-API SDK that's got your back when it comes to handling API keys and hooking up to databases.

It plays nice with both **sync and async** stuff right off the bat. That means it's perfect for all sorts of things these days, like AI APIs, Telegram bots, regular REST services, and automation tools.

Because it works hand-in-hand with things like `httpx` and `aiohttp`, has some neat logging features (you can even get alerts on Telegram if you want), and can store data in databases like MongoDB, Ryzenth is made for developers who want an API client that's easy to work with, can grow as needed, and can be tweaked to fit their needs.

## Features

- Works with both `sync` and `async` clients, so whatever you're using, it's got you covered.
- Makes it easy to handle API Keys right out of the box.
- Plays well with today's AI stuff like making images, searching, writing text and all that.
- Uses `httpx` to keep things moving fast.
- And more!

## Installation

```bash
pip3 install ryzenth[fast]
````
Or Just update from github
```bash
pip3 install git+https://github.com/TeamKillerX/Ryzenth.git
```

## Getting Started

### New chaining Support
- Use syntax `\`
- Allow using `&` for parameters
- You need to log in to [`ryzenths.dpdns.org`](https://ryzenths.dpdns.org)
```py
from Ryzenth import RyzenthAuthClient

response = await RyzenthAuthClient()\
.with_credentials("68750d3b92828xxxxxxxx", "sk-ryzenth-*")\
.use_tool("instatiktok")\
.set_parameter("&url={url}&platform=facebook")\
.retry(2)\
.cache(True)\
.timeout(10)\
.execute()

print(response)

# Optional Client:
clients = await RyzenthApiClient(tools_name=["ryzenth-v2"], api_key={"ryzenth-v2": [{}]}, rate_limit=100, use_default_headers=True)
```

### Ryzenth API without API Key
- Support Grok, OpenAI V2, vision, image generation

- **Chat ultimate** Supported Models: `grok`, `deepseek-reasoning`, `evil`, `unity`, `sur`, `rtist`, `hypnosis-tracy`, `llama-roblox`
```py
from Ryzenth import RyzenthTools

new = RyzenthTools()

# Chat ultimate
response_grok = await new.aio_client.chat.ask_ultimate("what is durov on telegram?", model="grok")

print(await response_grok.to_result())

# OpenAI V2
response_openai = await new.aio_client.chat.ask("What's the capital of Japan?")
print(await response_openai.to_result())

# After close
await new.aio_client.chat.close()

# Image generation
response_content = await new.aio_client.images.create("make a generate cat blue")

await response_content.to_save()

# Upload + Ask
response_see = await new.aio_client.images.create_upload_to_ask("Describe this image:", "/path/to/example.jpg")
await response_see.to_result()

# After close
await new.aio_client.images.close()
```
- New Method 🌟
```py
await new.aio_client.images.create()
await new.aio_client.images.create_gemini_and_captions()
await new.aio_client.images.create_gemini_to_edit("add background Lamborghini", "/path/to/example.jpg") # use response.to_buffer_and_list()
await new.aio_client.images.create_upload_to_ask()
await new.aio_client.images.create_multiple()
await new.aio_client.chat.ask()
await new.aio_client.chat.ask_ultimate()
```

### Tool for developers
Custom Name:
- `itzpire` (dead)
- `ryzenth`
- `ryzenth-v2`
- `siputzx`
- `fgsi`
- `onrender` (next auto free month)
- `deepseek`
- `cloudflare`
- `paxsenix`
- `exonity`
- `yogik` (dead)
- `ytdlpyton`
- `openai`
- `cohere`
- `claude`
- `grok`
- `alibaba`
- `gemini`
- `gemini-openai`

Example plugins: [`/dev/modules/paxsenix.py`](https://github.com/TeamKillerX/Ryzenth/blob/dev/modules/paxsenix.py)

Share domain module: [`/Ryzenth/_shared.py#L4`](https://github.com/TeamKillerX/Ryzenth/blob/83ea891711c89d3c53e646c866ee5137f81fcb4c/Ryzenth/_shared.py#L4)
```py
from Ryzenth import RyzenthApiClient

clients = RyzenthApiClient(
    tools_name=["siputzx"],
    api_key={"siputzx": [{"Authorization": f"Bearer test"}]},
    rate_limit=100,
    use_default_headers=True
)
# your logic code here
```

### Async Example (Deprecated)
- Old endpoint has been deprecated and will no longer be supported.
```python
from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

ryz = ApiKeyFrom(..., is_ok=True)

await ryz.aio.send_message(
    "hybrid",
    QueryParameter(
        query="hello world!"
    )
)
```

### Sync Example (Deprecated)
- Old endpoint has been deprecated and will no longer be supported.
```python
from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

ryz = ApiKeyFrom(..., is_ok=True)
ryz._sync.send_message(
    "hybrid",
    QueryParameter(
        query="hello world!"
    )
)
```

### Multi-Support
```py
from Ryzenth.tool import GrokClient

g = GrokClient(api_key="sk-grok-xxxx")

response = await g.chat_completions(
    messages=[
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        },
        {
            "role": "user",
            "content": "What is the meaning of life, the universe, and everything?"
        }
    ],
    model="grok-3-mini-latest",
    reasoning_effort="low",
    temperature=0.7,
    timeout=30
)
print(response)
```
## Tool Developer
~ Artificial Intelligence
- [`OpenAI`](https://platform.openai.com/docs) - OpenAI Docs
- [`Gemini AI`](https://ai.google.dev) - Gemini AI Docs
- [`Cohere AI`](https://docs.cohere.com/) - Cohere AI Docs
- [`Qwen AI`](https://www.alibabacloud.com/help/en/model-studio/use-qwen-by-calling-api) - Alibaba AI Docs
- [`Claude AI`](https://docs.anthropic.com/) - Claude AI Docs
- [`Grok AI key`](https://docs.x.ai/docs) - Grok AI Docs

## How to get api key?
- [`Ryzenth API key`](https://ryzenths.dpdns.org) - Website official
- [`Openai API key`](https://platform.openai.com/api-keys) - Website official
- [`Cohere API key`](https://dashboard.cohere.com/api-keys) - Website official
- [`Alibaba API key`](https://bailian.console.alibabacloud.com/?tab=playground#/api-key) - Website official
- [`Claude API key`](https://console.anthropic.com/settings/keys) - Website official
- [`Grok API key`](https://console.x.ai/team/default/api-keys) - Website official

## Credits

### Web Developers
- [`Paxsenix`](https://api.paxsenix.biz.id) - PaxSenix Dev
- [`Itzpire`](https://itzpire.com) - Itzpire Dev
- [`Ytdlpyton`](https://ytdlpyton.nvlgroup.my.id/) - Ytdlpyton Unesa Dev
- [`Exonity`](https://exonity.tech) - Exonity Dev
- [`Yogik`](https://api.yogik.id) - Yogik Dev (Dead)
- [`Siputzx`](https://api.siputzx.my.id) Siputzx Dev
- [`Fgsi`](https://fgsi.koyeb.app) Fgsi Dev (cewek)
- [`x-api-js`](https://x-api-js.onrender.com/docs) - Ryzenth DLR (JS) Dev
- [`Ryzenth V2`](https://ryzenths.dpdns.org) - Ryzenth V2 (TSX) Dev

*   Made with love by [xtdevs](https://t.me/xtdevs)
*   Got the idea from the early AkenoX API project
*   Big thanks to Google Dev tools for the AI stuff
*   The web scraper is all our own work

## Donation
Your gift makes a difference and lets us keep doing what we do

To donate using DANA, send your payment to Bank Jago account number `100201327349`.

Thanks a bunch!

## License
MIT License © 2025 Ryzenth Developers from TeamKillerX
