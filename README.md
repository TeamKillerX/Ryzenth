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

**Ryzenth** is a flexible Multi-API SDK with built-in support for API key management and database integration.

It supports both **synchronous and asynchronous** workflows out of the box, making it ideal for modern use cases such as AI APIs, Telegram bots, REST services, and automation tools.

With native integration for `httpx`, `aiohttp`, advanced logging (including optional Telegram alerts), and support for database storage like MongoDB, Ryzenth is designed for developers who need a lightweight, scalable, and customizable API client.

> Note: Ryzenth API V1 (**javascript**) is still alive and supported, but Ryzenth is the next generation.

## Features

- Full support for both `sync` and `async` clients
- Built-in API Key management
- Support for modern AI endpoints (image generation, search, text, and more)
- Designed for speed with `httpx`
- Etc

## Installation

```bash
pip install ryzenth[fast]
````

## Getting Started

### Async Example

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

### Sync Example

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

## Environment Variable Support
- Available API key v2 via [`@RyzenthKeyBot`](https://t.me/RyzenthKeyBot)

You can skip passing the API key directly by setting it via environment:

```bash
export RYZENTH_API_KEY=your-api-key
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
- [`Ryzenth API key`](https://t.me/RyzenthKeyBot) - Telegram bot
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
- [`x-api-js`](https://x-api-js.onrender.com/docs) - Ryzenth (JS) Dev
- [`Ryzenth TS`](https://ryzenth.randydev.my.id/v2/fast/list-endpoint) - Ryzenth (TS) Dev

* Built with love by [xtdevs](https://t.me/xtdevs)
* Inspired by early work on AkenoX API
* Thanks to Google Dev tools for AI integration concepts
* All Web scraper original

## Donation
* Your donation helps us continue our work!

To send payments via DANA, use the following Bank Jago account number:

Bank Jago: `100201327349`

## License
MIT License © 2025 Ryzenth Developers from TeamKillerX
