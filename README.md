# Ryzenth Library
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/Ryzenth)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/Ryzenth/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-GPL-pink)](https://github.com/TeamKillerX/Ryzenth/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Ryzenth - Version](https://img.shields.io/pypi/v/Ryzenth?style=round)](https://pypi.org/project/Ryzenth)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/Ryzenth/main.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/Ryzenth/main)

<div align="center">
    <a href="https://pepy.tech/project/Ryzenth"><img src="https://static.pepy.tech/badge/Ryzenth" alt="Downloads"></a>
    <a href="https://github.com/TeamKillerX/Ryzenth/workflows/"><img src="https://github.com/TeamKillerX/Ryzenth/actions/workflows/sync-tests.yml/badge.svg" alt="API Tests"/></a>
</div>

**Ryzenth** is a powerful and flexible Python SDK for interacting with the new **Ryzenth API V1**  a successor to the Ryzenth API V1 supporting both synchronous and asynchronous workflows out of the box.

> Note: Ryzenth API V1 (**javascript**) is still alive and supported, but Ryzenth is the next generation.

## Features

- Full support for both `sync` and `async` clients
- Built-in API Key management
- Support for modern AI endpoints (image generation, search, text, and more)
- Designed for speed with `httpx`

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

## Web scrapers
* [`itzpire`](https://itzpire.com) - Team Developer

## Credits

* Built with love by [xtdevs](https://t.me/xtdevs)
* Inspired by early work on AkenoX API
* Thanks to Google Dev tools for AI integration concepts
* All Web scraper original

## Donation
* Your donation helps us continue our work!

To send payments via DANA, use the following Bank Jago account number:

Bank Jago: `100201327349`

## License

You can now access the [`Ryzenth API V2 (Typescript)`](https://github.com/xtsea/akenox-ts-dev/blob/main/ryzenth-api.md#-existing-api-still-alive)
