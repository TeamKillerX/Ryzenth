# Ryzenth Library

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/Ryzenth)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/Ryzenth/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-MIT-pink)](https://github.com/TeamKillerX/Ryzenth/blob/dev/LICENSE)
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
**Ryzenth** is a powerful Multi-API SDK designed to seamlessly handle API keys and database connections with ease.

Built with `httpx` and `aiohttp` integration, comprehensive logging features (including Telegram alerts), and database storage capabilities like MongoDB, Ryzenth empowers developers with a flexible, scalable, and customizable API client solution.

## ✨ Features

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
- [ ] Hugging Face
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

## 🏆 Credits Developer
- **[xtdevs](https://t.me/xtdevs)** - Lead Developer & Creator
- **[Ryzenth V2](https://ryzenths.dpdns.org)** - Ryzenth TypeScript Solo Dev
- **TeamKillerX** - Solo Dev
- **AkenoX Project** - Original inspiration and foundation
- **Google Developer Tools** - AI integration support
- **Open Source Community** - Contributions and feedback
---

## 💖 Support Development

Your support helps us continue building and maintaining this project!

### 💰 Donation Options
- **Bank Transfer (DANA)**: Send to Bank Jago `100201327349`
- **Cryptocurrency**: Contact us for wallet addresses
- **GitHub Sponsors**: [Sponsor on GitHub](https://github.com/sponsors/TeamKillerX)

## Contact support
- You can ask to **contact support** [@zxyeor](https://t.me/zxyeor) via telegram
---

## 📄 License

**MIT License © 2025 Ryzenth Developers from TeamKillerX**

This project is open source and available under the [MIT License](https://github.com/TeamKillerX/Ryzenth/blob/dev/LICENSE).

---

<div align="center">

### 🌟 Star us on GitHub if you find this project useful!

[![GitHub stars](https://img.shields.io/github/stars/TeamKillerX/Ryzenth?style=social)](https://github.com/TeamKillerX/Ryzenth)
[![GitHub forks](https://img.shields.io/github/forks/TeamKillerX/Ryzenth?style=social)](https://github.com/TeamKillerX/Ryzenth/fork)
[![GitHub watchers](https://img.shields.io/github/watchers/TeamKillerX/Ryzenth?style=social)](https://github.com/TeamKillerX/Ryzenth)

**Made with ❤️ by the Ryzenth Solo Dev**

</div>
