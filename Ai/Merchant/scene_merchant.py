import warnings

from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.chat_models import Llama2Chat
from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from os.path import expanduser
from langchain_community.llms import LlamaCpp
from Ai.Merchant.scene_merchant_misc import template
from Misc import global_vars


class SceneMerchant:
    def __init__(self):
        self.model_path = expanduser(global_vars.model_path)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.template_messages = [
            SystemMessage(content=template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{text}"),
        ]
        self.prompt_template = ChatPromptTemplate.from_messages(self.template_messages)

    def load_llm(self):
        llm = LlamaCpp(
            model_path=self.model_path,
            streaming=False,
            verbose=False
        )
        llm_model = Llama2Chat(llm=llm)
        return llm_model

    def create_chain(self):
        llm_model = self.load_llm()
        chain = LLMChain(llm=llm_model, prompt=self.prompt_template, memory=self.memory)
        return chain
