class RyzenthMessage:
    @staticmethod
    def core(content: str):
        return {"role": "system", "content": content}

    @staticmethod
    def user(content: str):
        return {"role": "user", "content": content}

    @staticmethod
    def user_and_audio(
        content: str,
        format: str = "wav",
        audio_data=None,
        use_legacy_format=False
    ):
        if audio_data is None:
            return None
        if use_legacy_format:
            return {
                "role": "user",
                "content": [
                    {"type": "text", "text": content},
                    {"type": "input_audio", "input_audio": {"data": audio_data, "format": format}}
                ]
            }
        return {
            "role": "user",
            "content": [
                {"type": "input_text", "text": content},
                # base64 "data:image/jpeg;base64,"
                {"type": "input_audio", "input_audio": {"data": audio_data, "format": format}}
            ]
        }

    @staticmethod
    def user_and_image(content: str, fn=None, use_legacy_format=False):
        if fn is None:
            return None
        if use_legacy_format:
            return {
                "role": "user",
                "content": [
                    {"type": "text", "text": content},
                    {"type": "image_url", "image_url": {"url": fn}}  # url or base64 "data:image/jpeg;base64,"
                ]
            }
        return {
            "role": "user",
            "content": [
                {"type": "input_text", "text": content},
                {"type": "input_image", "image_url": fn}  # url or base64 "data:image/jpeg;base64,"
            ]
        }

    @staticmethod
    def assistant(content: str):
        return {"role": "assistant", "content": content}
