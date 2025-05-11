# Ryzenth Library

**Ryzenth** is a powerful and flexible Python SDK for interacting with the new **Ryzenth API**  a successor to the AkenoX API supporting both synchronous and asynchronous workflows out of the box.

> Note: AkenoX API is still alive and supported, but Ryzenth is the next generation.

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

ryz = ApiKeyFrom("your-api-key")

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

ryz = ApiKeyFrom("your-api-key")
ryz._sync.send_message(
    "hybrid",
    QueryParameter(
        query="hello world!"
    )
)
```

## Environment Variable Support
- Available API key v2 via [`@aknuserbot`](https://t.me/aknuserbot)

You can skip passing the API key directly by setting it via environment:

```bash
export RYZENTH_API_KEY=your-api-key
```

## Credits

* Built with love by [xtdevs](https://t.me/xtdevs)
* Inspired by early work on AkenoX API
* Thanks to Google Dev tools for AI integration concepts

## License

Private – API still in early access stage. Public release coming soon.
