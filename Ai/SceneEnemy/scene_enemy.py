from langchain.chains.llm import LLMChain
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.prompts import FewShotPromptTemplate
from Ai.SceneEnemy import scene_enemy_misc as es
from Ai.ai_model import AiModel

scene_enemy = None

class SceneEnemy(AiModel):
    def __init__(self):
        super().__init__()

        self.load_prompt()
        self.load_llm()
        self.chain = self.create_chain()

    def load_prompt(self):
        self.prompt = FewShotPromptTemplate(
            examples=es.examples,
            example_prompt=es.example_prompt,
            prefix=es.prefix,
            suffix=es.suffix,
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


def initialize_scene_enemy():
    global scene_enemy
    scene_enemy = SceneEnemy()
    scene_enemy.create_scene("Write 'Loading scene'")
