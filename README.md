<img src="https://cdn.ryzenths.dpdns.org/ryzenth.jpg">

<p align="center">
  <a aria-label="Ryzenth logo" href="https://ryzenths.dpdns.org">
    <img src="https://badgen.net/badge/icon/Made%20by%20Ryzenth?icon=terminal&label&color=black&labelColor=black">
  </a>
  <br/>
  <a aria-label="Ryzenth Docs" href="https://api.ryzenths.dpdns.org/api-doc">
    <img src="https://badgen.net/badge/icon/Ryzenth Docs API?icon=bitcoin-lightning&label&color=blue&labelColor=red">
  </a>
</p>

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/Ryzenth)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/Ryzenth/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-MIT-pink)](https://github.com/TeamKillerX/Ryzenth/blob/dev/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Ryzenth - Version](https://img.shields.io/pypi/v/Ryzenth?style=round)](https://pypi.org/project/Ryzenth)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/Ryzenth/dev.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/Ryzenth/dev)
[![github.workflows](https://github.com/TeamKillerX/Ryzenth/actions/workflows/async-tests.yml/badge.svg)](https://github.com/TeamKillerX/Ryzenth/workflows/)


<div align="center">
    <a href="https://pepy.tech/project/Ryzenth"><img src="https://static.pepy.tech/badge/Ryzenth" alt="Downloads"></a>
</div>

---
**Ryzenth** is a powerful Multi-API SDK designed to seamlessly handle API keys and database connections with ease.

## Key Features

- **Dual Mode Support**: Works with both `sync` and `async` clients
- **Smart API Key Management**: Built-in API key handling and rotation
- **AI-Ready**: Seamless integration with modern AI services (image generation, text processing, etc.)
- **High Performance**: Built on `httpx` for optimal speed and reliability
- **Comprehensive Logging**: Built-in logging with optional Telegram notifications
- **Error Handling**: Robust error handling with automatic retries
- **Context Managers**: Proper resource management with async context support
- **Database Integration**: MongoDB and other database connectors included

## Installation

### Standard Installation
```bash
pip3 install ryzenth[fast]
```

### Development Installation (Latest Features)
```bash
pip3 install git+https://github.com/TeamKillerX/Ryzenth.git
```

## Quick Start
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools()
chat = rt.aio.chat

results = await chat.kimi_ask(
    [chat.msg.user("hello World")],
    use_instruct=True
)

obj = await results.to_obj()
print(obj.data.choices[0].message.content)
```
## Usage
### Text & Images in one conversation
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools()

chat = rt.aio.chat

results = await chat.ask(
    [
        chat.msg.core("You are a helpful assistant"),
        chat.msg.user_and_image(
            "What's in this picture?",
            "data:image/jpeg;base64," + chat.file.encode_image_base64("examples/path/create.jpg"),
            use_legacy_format=True
        )
    ],
    use_conversation=True
)

print(await results.to_dict())
```

## OpenAI compatibility
- Support endpoints:
- `https://api.ryzenths.dpdns.org/api/v1/chat/completions`
- `https://api.ryzenths.dpdns.org/api/v1/responses`

You can use source code [OpenAI Python SDK on GitHub](https://github.com/openai/openai-python) or [OpenAI Javascript SDK on GitHub](https://github.com/openai/openai-node)

**List Models:**

`chat.completions` (only)
1. `qwen-plus`
2. `openai/gpt-oss-20b`
3. `moonshotai/kimi-k2-instruct` (**speed recommend**)
4. `meta-llama/llama-guard-4-12b`
5. `meta-llama/llama-4-scout-17b-16e-instruct`
6. `ryzenth-web-compatibility`
7. `gemini-2.0-flash`

`responses` (only)
1. `llama-3.3-70b-versatile` (**speed recommend**)
2. `gpt-5`
3. `gpt-5-mini`
4. `gpt-5-nano`
5. `ryzenth-ingalesh`
6. `ryzenth-darknet`
7. `ryzenth-ultraCEO`
8. `ryzenth-otakuAI`

Javascript Code
```js
import OpenAI from 'openai';

const clients = new OpenAI({
  apiKey: "apikey-required",
  baseURL: "https://api.ryzenths.dpdns.org/api/v1"
});

const response = await clients.responses.create({
  model: 'gpt-5',
  input: [
    {
      role: "developer",
      content: "Talk like a pirate."
    },
    {
      role: "user",
      content: "Are semicolons optional in JavaScript?",
    }
  ]
});

const completion = await clients.chat.completions.create({
  model: 'moonshotai/kimi-k2-instruct',
  messages: [
    { role: 'system', content: 'Talk like a pirate.' },
    { role: 'user', content: "What's your name?" },
  ],
});

console.log(completion.choices[0].message.content);
console.log(response.output_text);
```

## Platform full support
- [x] Claude
- [x] OpenAI
- [x] Gemini-Openai
- [x] Gemini
- [x] Cohere
- [x] Grok
- [x] Deepseek
- [x] Cloudflare
- [x] Qwen
- [x] Zai
- [x] Hugging Face
- [x] Kimi AI
- [x] GPT oss
- [x] Meta Llama
- [x] Ryzenth (Free)
- [x] Image Generate
- [x] Flux AI
- [x] All in one downloader

---

## Troubleshoot

Sometimes errors occur, but we are here to help This guide covers some of the most common issues we’ve seen and how you can resolve them. However, this guide isn’t meant to be a comprehensive collection of every Ryzenth issue. For more help with troubleshooting your issue, try:

- [Terms of service](https://ryzenths.dpdns.org/terms-policy)
- [Ryzenth Support](https://ryzenths.dpdns.org/contact)
- [Github Issues](https://github.com/TeamKillerX/Ryzenth/issues)

- `support@ryzenths.dpdns.org` - [`here`](https://github.com/TeamKillerX/Ryzenth?tab=readme-ov-file#contact-support)

## Credits Developer
- **[xtdevs](https://t.me/xtdevs)** - Lead Developer & Creator
- **[Ryzenth V2](https://ryzenths.dpdns.org)** - Ryzenth TypeScript Author @xtsea
- **TeamKillerX** - Author @xtsea
- **Google Developer Tools** - AI integration support
- **Open Source Community** - Contributions and feedback
---

## Contact support
- You can ask to **contact support** [@zxyeor](https://t.me/zxyeor) via telegram
---

## License

**MIT License © 2025 Ryzenth Developers from TeamKillerX**

This project is open source and available under the [MIT License](https://github.com/TeamKillerX/Ryzenth/blob/dev/LICENSE).

---
