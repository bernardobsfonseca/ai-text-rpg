from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler


class AiModel:
    def __init__(self):
        self.prompt = None
        self.llm = None
        self.chain = None
        self.callback_manager = CallbackManager(
            [StreamingStdOutCallbackHandler()])

    def load_prompt(self):
        pass

    def load_llm(self):
        pass

    def create_chain(self):
        pass
