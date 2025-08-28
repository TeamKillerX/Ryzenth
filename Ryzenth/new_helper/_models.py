class RyzenthMessage:
    @staticmethod
    def core(content: str):
        return {"role": "system", "content": content}

    @staticmethod
    def user(content: str):
        return {"role": "user", "content": content}

    @staticmethod
    def user_and_image(content: str, base64Image, use_legacy_format=False):
        return {
            "role": "user",
            "content": [
                {"type": "text", "text": content},
                {"type": "input_image", "image_url": {
                    "url": f"data:image/jpeg;base64,{base64Image}"}}
            ]
        }
        } if use_legacy_format else {
            "role": "user",
            "content": [
                {"type": "input_text", "text": content},
                {"type": "input_image",
                 "image_url": f"data:image/jpeg;base64,{base64Image}"}
            ]
        }


    @ staticmethod
    def assistant(content: str):
        return {"role": "assistant", "content": content}
