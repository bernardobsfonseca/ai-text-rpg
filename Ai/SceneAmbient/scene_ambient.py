from langchain.chains.llm import LLMChain
from langchain_community.llms import LlamaCpp
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from Ai.SceneAmbient import scene_ambient_misc as ms
from Ai.ai_model import AiModel

scene_ambient = None


class SceneAmbient(AiModel):
    def __init__(self):
        super().__init__()

        self.load_prompt()
        self.load_llm()
        self.chain = self.create_chain()

    def load_prompt(self):
        self.prompt = FewShotPromptTemplate(
            examples=ms.examples,
            example_prompt=ms.example_prompt,
            prefix=ms.prefix,
            suffix=ms.suffix,
            input_variables=["scene"]
        )

    def load_llm(self):
        self.llm = LlamaCpp(
            model_path="C:/Unesp/TCC/Models/llama-2-7b-chat.Q4_K_M.gguf",
            temperature=0,
            max_tokens=500,
            callback_manager=self.callback_manager,
            verbose=False,
        )

    def create_chain(self):
        chain = LLMChain(
            prompt=self.prompt,
            llm=self.llm
        )

        return chain

    def create_scene(self, scene: str):
        self.chain.invoke({"scene": scene})


def initialize_scene_embient():
    global scene_ambient
    scene_ambient = SceneAmbient()
    scene_ambient.create_scene("Write 'Loading scene'")