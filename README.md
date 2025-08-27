# Ryzenth Library

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/Ryzenth)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/Ryzenth/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-MIT-pink)](https://github.com/TeamKillerX/Ryzenth/blob/dev/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Ryzenth - Version](https://img.shields.io/pypi/v/Ryzenth?style=round)](https://pypi.org/project/Ryzenth)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/Ryzenth/dev.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/Ryzenth/dev)
[![Pylint](https://github.com/TeamKillerX/Ryzenth/actions/workflows/pylint.yml/badge.svg?branch=dev)](https://github.com/TeamKillerX/Ryzenth/actions/workflows/pylint.yml)


<div align="center">
    <a href="https://pepy.tech/project/Ryzenth"><img src="https://static.pepy.tech/badge/Ryzenth" alt="Downloads"></a>
    <a href="https://github.com/TeamKillerX/Ryzenth/workflows/"><img src="https://github.com/TeamKillerX/Ryzenth/actions/workflows/async-tests.yml/badge.svg" alt="API Tests"/></a>
</div>

---

![Image](https://github.com/user-attachments/assets/ebb42582-4d5d-4f6a-8e8b-78d737810510)

---

**Ryzenth** is a powerful Multi-API SDK designed to seamlessly handle API keys and database connections with ease.

It provides native support for both **synchronous and asynchronous** operations, making it ideal for modern applications including AI APIs, Telegram bots, REST services, and automation tools.

Built with `httpx` and `aiohttp` integration, comprehensive logging features (including Telegram alerts), and database storage capabilities like MongoDB, Ryzenth empowers developers with a flexible, scalable, and customizable API client solution.

## 🚨 Important Notes

### HTTP 403 Error Fix
If you're encountering **403 Forbidden** errors, ensure you're setting proper headers:

```python
# ✅ CORRECT - Always use proper headers
from Ryzenth import RyzenthApiClient

clients = RyzenthApiClient(
    tools_name=["your-tool"],
    api_key={"your-tool": [{"Authorization": "Bearer your-token"}]},
    rate_limit=100,
    use_default_headers=True  # 🔥 IMPORTANT: Set this to True
)

# ✅ CORRECT - Custom headers example
clients = RyzenthApiClient(
    tools_name=["your-tool"],
    api_key={"your-tool": [{
        "Authorization": "Bearer your-token",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }]},
    rate_limit=100,
    use_default_headers=True
)

# ❌ WRONG - Missing headers will cause 403 errors
clients = RyzenthApiClient(
    tools_name=["your-tool"],
    api_key={"your-tool": [{}]},  # Empty headers
    use_default_headers=False     # No default headers
)
```

### Required Headers Format
The library automatically adds these headers when `use_default_headers=True`:
- `User-Agent: Ryzenth/Python v-{version}`
- `Accept: application/json`
- `Content-Type: application/json`

### Javascript Your own API
```js
const ua = req.headers['User-Agent'];
const gh = req.headers['X-Github-Source'];
const ghVersion = req.headers['X-Ryzenth-Version'];

console.log(gh) // check valid whitelist TeamKillerX/Ryzenth
```

## ✨ Features

- 🔄 **Dual Mode Support**: Works with both `sync` and `async` clients
- 🔐 **Smart API Key Management**: Built-in API key handling and rotation
- 🤖 **AI-Ready**: Seamless integration with modern AI services (image generation, text processing, etc.)
- ⚡ **High Performance**: Built on `httpx` for optimal speed and reliability
- 📊 **Comprehensive Logging**: Built-in logging with optional Telegram notifications
- 🛡️ **Error Handling**: Robust error handling with automatic retries
- 🎯 **Context Managers**: Proper resource management with async context support
- 📦 **Database Integration**: MongoDB and other database connectors included

## 📦 Installation

### Standard Installation
```bash
pip3 install ryzenth[fast]
```

### Development Installation (Latest Features)
```bash
pip3 install git+https://github.com/TeamKillerX/Ryzenth.git
```

## 🚀 Quick Start

### 🔗 New Chaining API Support
Modern fluent API with method chaining:

```python
from Ryzenth import RyzenthAuthClient

# 🌟 Fluent API with chaining
response = await RyzenthAuthClient()\
    .with_credentials("68750d3b92828xxxxxxxx", "sk-ryzenth-*")\
    .use_tool("instatiktok")\
    .set_parameter("&url={url}&platform=facebook")\
    .retry(2)\
    .cache(True)\
    .timeout(10)\
    .execute()

print(response)

# 🔧 Traditional client approach
clients = await RyzenthApiClient(
    tools_name=["ryzenth-v2"],
    api_key={"ryzenth-v2": [{}]},
    rate_limit=100,
    use_default_headers=True
)
```

### 🔥 Multi Client Tools
- support environment
```py
# COHERE_API_KEY
# GEMINI_API_KEY
# XAI_API_KEY
# OPENAI_API_KEY
# ALIBABA_API_KEY
# DEEPSEEK_API_KEY
# ZAI_API_KEY

from Ryzenth import RyzenthTools

rt = RyzenthTools()
# your own code logic
```
## Attribute Tools
```py
.aio.grok_chat
.aio.claude_chat
.aio.gemini_chat
.aio.old_gemini_chat
.aio.openai_images
.aio.openai_responses
.aio.qwen_chat
.aio.deepseek_chat
.aio.zai_chat
.aio.qwen_images
.aio.qwen_videos
.aio.images
.aio.chat
```

## Examples full code
### gemini-openai tools
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools("api-key-from-gemini")

results = await rt.aio.gemini_chat.ask([
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is Gemini?"}
], model="gemini-2.5-flash")

print(await results.to_dict())
```
- Use tools
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools("api-key-from-gemini")

results = await rt.aio.gemini_chat.ask([
    {"role": "user", "content": "What's the weather like in Chicago today?"}
], tools=[
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. Chicago, IL"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    }
  }
],tool_choice="auto")

print(await results.to_json_dumps())
```

### qwen-image tools
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools("api-key-from-qwen")

response = await rt.aio.qwen_images.create("make a generate cat blue and background car Lamborghini gold")

output = await response.run()

img = await response.to_buffer_request(output.results[0].url)

print(img)
```
- Use task id manually
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools()

response = await rt.aio.qwen_images.create("...")
obj = await response.to_obj()
task_id = obj.output.task_id

response_status = await rt.aio.qwen_images.get_task(task_id)

obj_res = await response_status.to_obj()

if obj_res.output.task_status == "SUCCEEDED":
    print(obj_res.output)
```

### Ryzenth-Chat tools (Free)
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools()

results = await rt.aio.chat.ask([
    {"role": "system", "content": "You are helpful assistant"},
    {"role": "user", "content": "oh good job"}
], use_conversation=True)

print(await results.to_json_dumps())
```
- Use Kimi AI (free)
- support `use_instruct` for multi turn conversation
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools()

results = await rt.aio.chat.ask_kimi([
    {"role": "system", "content": "...."},
    {"role": "user", "content": "hello world!"}
], use_instruct=True)

obj = await results.to_obj()
print(obj.data.choices[0].message.content)
```
- You can use one prompt
```py
from Ryzenth import RyzenthTools

rt = RyzenthTools()

results = await rt.aio.chat.ask("Hello world")

print(await results.to_json_dumps())
```

### 🤖 AI Features (No API Key Required)
Supports multiple AI models: `grok`, `deepseek-reasoning`, `evil`, `unity`, `sur`, `rtist`, `hypnosis-tracy`, `llama-roblox`

```python
from Ryzenth import RyzenthTools

rt = RyzenthTools()

# 💬 Chat Ultimate - Multiple AI Models
response_grok = await rt.aio.chat.ask_ultimate(
    "What is Durov's role in Telegram?",
    model="grok"
)
print(await response_grok.to_result())

# 🎯 OpenAI V2 Integration
response_openai = await rt.aio.chat.ask("What's the capital of Japan?")
print(await response_openai.to_result())

# 🎨 Image Generation
response_content = await rt.aio.images.create("generate a blue cat")
await response_content.to_save()

# 👀 Image Analysis with Upload
response_see = await rt.aio.images.create_upload_to_ask(
    "Describe this image:",
    "/path/to/example.jpg"
)
result = await response_see.to_result()

# 🧹 Proper cleanup
await rt.aio.chat.close()
await rt.aio_client.images.close()
```

### 🎥 Advanced AI Features

```python
# 🖼️ Multiple image operations
await rt.aio.images.create()
await rt.aio.images.create_gemini_and_captions()
await rt.aio_client.images.create_gemini_to_edit(
    "add Lamborghini background",
    "/path/to/example.jpg"
)  # Use response.to_buffer_and_list()

await rt.aio.images.create_upload_to_ask()
await rt.aio.images.create_multiple()

# 💭 Chat operations
await rt.aio.chat.ask()
await rt.aio.chat.ask_ultimate()
```

---

## 🎬 Image & Video Generation with Qwen AI

Generate high-quality images and videos using **Qwen AI** with dot notation access:

```python
from Ryzenth import RyzenthTools

rt = RyzenthTools("your-qwen-api-key")

# 🖼️ Generate Image
response = await rt.aio.qwen_images.create("generate a blue cat running")
output = await response.create_task_and_wait(max_retries=120, poll_interval=1.0)

print("🎨 Image URL:", output.results[0].url)

# 🎬 Generate Video
response_video = await rt.aio.qwen_videos.create("blue cat running in slow motion")
output_video = await response_video.create_task_and_wait(max_retries=120, poll_interval=1.0)

print("🎥 Video URL:", output_video.video_url)
```

> **⚠️ Version Note**: Dot notation access may be limited in version `2.2.3+` due to API changes. Check our [GitHub Discussions](https://github.com/TeamKillerX/Ryzenth/discussions) for updates.

---

## 🛠️ Developer Tools & Supported APIs

## Pricing & Free Tier (Ryzenth)

| Endpoints | Free | Description |
|-----------|--------|-------------|
| `kimi-latest` | ✅ Free | Kimi AI |
| `openai-v2/oss` | ✅ Free | GPT oss |
| `ultimate-chat` | ✅ Free | Custom Model |
| `openai-v2` | ✅ Free | openAI |
| `openai-v2/image-vision` | ✅ Free | openAI image vision |
| `gemini-latest/imagen/edit` | ✅ Free | Gemini imagen edit |
| `gemini-latest/imagen` | ✅ Free | Gemini imagen |
| `tools/generate-image` | ✅ Free | Tool Generate image |

### Available API Tools
Choose from our extensive list of supported APIs:

| Tool Name | Status | Description |
|-----------|--------|-------------|
| `itzpire` | ❌ Dead | Legacy API service |
| `ryzenth` | ✅ Active | Main Ryzenth API |
| `ryzenth-v2` | ✅ Active | Enhanced Ryzenth API |
| `siputzx` | ✅ Active (Auto block) | Community API |
| `fgsi` | ✅ Active | FGSI API Service |
| `onrender` | ✅ Active | Render-based API |
| `deepseek` | ✅ Active | DeepSeek AI API |
| `cloudflare` | ✅ Active | Cloudflare Workers API |
| `paxsenix` | ✅ Active | PaxSenix API |
| `exonity` | ✅ Active | Exonity API |
| `yogik` | ❌ Dead | Legacy API |
| `ytdlpyton` | ✅ Active | YouTube downloader |
| `openai` | ✅ Active | OpenAI API |
| `cohere` | ✅ Active | Cohere AI API |
| `claude` | ✅ Active | Anthropic Claude API |
| `grok` | ✅ Active | Grok AI API |
| `alibaba` | ✅ Active | Alibaba Qwen API |
| `gemini` | ✅ Active | Google Gemini API |
| `gemini-openai` | ✅ Active | Gemini OpenAI Compatible |

### 🔧 Custom API Implementation

```python
from Ryzenth import RyzenthApiClient

# 🎯 Example with SiputZX API
clients = RyzenthApiClient(
    tools_name=["siputzx"],
    api_key={"siputzx": [{"Authorization": "Bearer test"}]},
    rate_limit=100,
    use_default_headers=True  # 🔥 Always enable for 403 fix
)

# Your implementation logic here
response = await clients.get(
    tool="siputzx",
    path="/api/endpoint",
    params={"query": "your-query"}
)
```

> **📚 Resources**:
> - Example plugins: [`/dev/modules/paxsenix.py`](https://github.com/TeamKillerX/Ryzenth/blob/dev/modules/paxsenix.py)
> - Shared domains: [`/Ryzenth/_shared.py#L4`](https://github.com/TeamKillerX/Ryzenth/blob/83ea891711c89d3c53e646c866ee5137f81fcb4c/Ryzenth/_shared.py#L4)

---

## 🏗️ Legacy Examples (Deprecated)

### Async Example
```python
from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

ryz = ApiKeyFrom(..., is_ok=True)

await ryz.aio.send_message(
    "hybrid",
    QueryParameter(query="hello world!")
)
```

### Sync Example
```python
from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

ryz = ApiKeyFrom(..., is_ok=True)
ryz._sync.send_message(
    "hybrid",
    QueryParameter(query="hello world!")
)
```

---

## 🤖 Multi-Platform AI Support

### Grok AI Integration
```python
from Ryzenth.tool import GrokClient

g = GrokClient(api_key="sk-grok-xxxx")

response = await g.chat_completions(
    messages=[
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy."
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

---

## 🔑 API Keys & Documentation

### 🤖 AI Platform Documentation
- **OpenAI**: [Platform Documentation](https://platform.openai.com/docs)
- **Google Gemini**: [AI Development Guide](https://ai.google.dev)
- **Cohere**: [API Documentation](https://docs.cohere.com/)
- **Alibaba Qwen**: [Model Studio Guide](https://www.alibabacloud.com/help/en/model-studio/use-qwen-by-calling-api)
- **Anthropic Claude**: [API Reference](https://docs.anthropic.com/)
- **Grok AI**: [X.AI Documentation](https://docs.x.ai/docs)

### 🔐 Get Your API Keys
| Platform | Get API Key | Official Website |
|----------|-------------|------------------|
| **Ryzenth** | [Get Key](https://ryzenths.dpdns.org) | Official Ryzenth Portal |
| **OpenAI** | [Get Key](https://platform.openai.com/api-keys) | OpenAI Platform |
| **Cohere** | [Get Key](https://dashboard.cohere.com/api-keys) | Cohere Dashboard |
| **Alibaba** | [Get Key](https://bailian.console.alibabacloud.com/?tab=playground#/api-key) | Alibaba Console |
| **Claude** | [Get Key](https://console.anthropic.com/settings/keys) | Anthropic Console |
| **Grok** | [Get Key](https://console.x.ai/team/default/api-keys) | X.AI Console |

---

### 🌐 API Provider Partners (NB Friends)
- **[PaxSenix](https://api.paxsenix.biz.id)** - PaxSenix
- **[Itzpire](https://itzpire.com)** - Itzpire
- **[Ytdlpyton](https://ytdlpyton.nvlgroup.my.id/)** - Unesa
- **[Exonity](https://exonity.tech)** - Exonity
- **[Yogik](https://api.yogik.id)** - Yogik (Legacy)
- **[Siputzx](https://api.siputzx.my.id)** - Siputzx
- **[FGSI](https://fgsi.koyeb.app)** - FGSI

## 🏆 Credits Developer
- **[xtdevs](https://t.me/xtdevs)** - Lead Developer & Creator
- **[X-API-JS](https://x-api-js.onrender.com/docs)** - Ryzenth DLR JavaScript Solo Dev
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

Every contribution, no matter the size, makes a difference! 🚀

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
