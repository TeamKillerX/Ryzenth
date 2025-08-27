# Expired 2026 💀
UNKNOWN_TEST = "YWtlbm9fVUtRRVFNdDk5MWtoMkVoaDdKcUpZS2FweDhDQ3llQw=="

TOOL_DOMAIN_MAP = {
    "itzpire": "https://itzpire.com",
    "ryzenth": "https://ryzenth-api.onrender.com",
    "ryzenth-v2": "https://api.ryzenths.dpdns.org",
    "siputzx": "https://api.siputzx.my.id",
    "fgsi": "https://fgsi.koyeb.app",
    "onrender": "https://x-api-js.onrender.com",
    "deepseek": "https://api.deepseek.com",
    "cloudflare": "https://api.cloudflare.com",
    "paxsenix": "https://api.paxsenix.biz.id",
    "exonity": "https://exonity.tech",
    "yogik": "https://api.yogik.id",
    "ytdlpyton": "https://ytdlpyton.nvlgroup.my.id",
    "openai": "https://api.openai.com/v1",
    "cohere": "https://api.cohere.com",
    "claude": "https://api.anthropic.com/v1",
    "grok": "https://api.x.ai/v1",
    "alibaba": "https://dashscope-intl.aliyuncs.com",
    "gemini": "https://generativelanguage.googleapis.com/v1beta",
    "gemini-openai": "https://generativelanguage.googleapis.com/v1beta/openai",
    "zai": "https://api.z.ai"
}

### -------------AI-----------------###

# GROK AI
"""
headers = {
    'accept: application/json',
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
grok_response = await clients.post(
    tool="grok",
    path="/chat/completions",
    json={
        "model": "grok-3",
        "messages": [
            {"role": "user", "content": "hello world!"}
        ],
        "temperature": 0.7
    }
)
"""


# COHERE
"""
headers = {
    'accept: application/json',
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
cohere_response = await clients.post(
    tool="cohere",
    path="/chat",
    json={
        "chat_history": [],
        "message": "What year was he born?",
        "connectors": [{"id": "web-search"}]
    }
)
"""

# ALIBABA
"""
headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
alibaba_response = await clients.post(
    tool="alibaba",
    path="/chat/completions",
    json={
        "model": "qwen-plus",
        "messages": [
            {"role": "user", "content": "hello world!"}
        ],
        "temperature": 0.7
    }
)
"""

# DEEPSEEK
"""
headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
deepseek_response = await clients.post(
    tool="deepseek",
    path="/chat/completions",
    json={
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "hello world!"}
        ],
        "temperature": 0.7
    }
)
"""
### -------------END AI-----------------###

# this API is different
BASE_DICT_RENDER = {
    "transcript": "transcript-dl",  # url #render
    "pinterest": "pinterest-dl",  # url #render
    "fbvideo": "fbvideo-dl",  # url #render
    "fbphoto": "fbphoto-dl",  # url #render
    "tiktok": "tiktok-dl",  # url #render
    "youtube-mp3": "youtube-mp3-dl",  # url #render
    "youtube-mp4": "youtube-mp4-dl",  # url #render
    "instagram": "instagram-dl",  # url # render
    "lyrics-search": "lyrics-search-dl",  # query #render
    "yt-search": "yt-search-dl",  # query #render
    "google-search": "google-search-dl",  # query #render
    "pinterest-search": "pinterest-search-dl",  # query #render
    "tiktok-search": "tiktok-search-dl",  # query #render
    "yt-username": "yt-username",  # username #render
    "tiktok-username": "tiktok-username",  # username #render
    "xnxx-dl": "xnxx-dl",  # types optional #render
    "hentai-anime": "hentai-anime"  # None, render
}

BASE_DICT_OFFICIAL = {
    "teraboxv4": "terabox-v4",
    "twitterv3": "twitter-v3",
    "xnxxinfov2": "xnxx-info-v2",
    "instagramv4": "instagram-v4",
    "instagramv3": "instagram-v3",
    "instagramv2": "instagram-v2",
    "instagram-v0": "instagram",
    "twitter": "twitter",
    "tiktok-v0": "tiktok",
    "tiktokv2": "tiktok-v2",
    "facebook": "fb",
    "snapsave": "snapsave",
    "savefrom": "savefrom"
}

BASE_DICT_AI_RYZENTH = {
    "hybrid": "AkenoX-1.9-Hybrid",
    "hybrid-english": "AkenoX-1.9-Hybrid-English",
    "melayu": "lu-melayu",
    "nocodefou": "nocodefou",
    "mia": "mia-khalifah",
    "curlmcode": "curl-command-code",
    "quotessad": "quotes-sad",
    "quoteslucu": "quotes-lucu",
    "lirikend": "lirik-end",
    "alsholawat": "al-sholawat"
}
