# Ryzenth Library
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/Ryzenth)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/Ryzenth/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-GPL-pink)](https://github.com/TeamKillerX/Ryzenth/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Ryzenth - Version](https://img.shields.io/pypi/v/Ryzenth?style=round)](https://pypi.org/project/Ryzenth)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/Ryzenth/main.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/Ryzenth/main)

**Ryzenth** is a powerful and flexible Python SDK for interacting with the new **Ryzenth API V1**  a successor to the AkenoX API supporting both synchronous and asynchronous workflows out of the box.

> Note: Ryzenth API V1 is still alive and supported, but Ryzenth is the next generation.

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

ryz = ApiKeyFrom(..., is_free_from_ryzenth=True)

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

ryz = ApiKeyFrom(..., is_free_from_ryzenth=True)
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

## Credits

* Built with love by [xtdevs](https://t.me/xtdevs)
* Inspired by early work on AkenoX API
* Thanks to Google Dev tools for AI integration concepts

## License

You can now access the [`Ryzenth API (Typescript)`](https://github.com/xtsea/akenox-ts-dev/blob/main/ryzenth-api.md#-existing-api-still-alive)
