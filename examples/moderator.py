# Created by https://t.me/RendyProjects
# Fix dict spamming user ID different

from Ryzenth import ApiKeyFrom

ryz = ApiKeyFrom(..., is_free_from_ryzenth=True)

ryz.aio.timeout = 10

async def aigen_image_check(user_id: int, text: str):
    result = {}
    try:
        response = await ryz.aio.moderator.aigen_image_check(
            text=text,
            version="v2",
            is_loads=True,
            dot_access=False
        )
        result[user_id] = {
            "is_image": response.get("is_image", False),
            "prompt": response.get("prompt", ""),
            "is_anti_porno": response.get("is_anti_porno", False),
            "reason": response.get("reason", "")
        }
        return result
    except Exception:
        return {user_id: {
            "is_image": False,
            "prompt": "",
            "is_anti_porno": False,
            "reason": ""
        }}

# example usage:
image_data = await aigen_image_check(message.from_user.id, message.text)
image_result = image_data.get(message.from_user.id, {})

if image_result.get("is_image"):
    return image_result["prompt"]
if image_result.get("is_anti_porno"):
    return image_result["reason"]
