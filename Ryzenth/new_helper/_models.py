class RyzenthMessage:
    @staticmethod
    def core(content: str):
        return {"role": "system", "content": content}

    @staticmethod
    def user(content: str):
        return {"role": "user", "content": content}

    @staticmethod
    def assistant(content: str):
        return {"role": "assistant", "content": content}
