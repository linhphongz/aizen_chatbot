from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferWindowMemory

from prompt_template import memory_template

import os
from dotenv import load_dotenv
load_dotenv()

# Set the Google API key from environment variables
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

# Function to initialize the Google Generative AI model
def llm():
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    return llm

# Function to create conversation memory with a buffer window
def chat_memory(chat_history):
    return ConversationBufferWindowMemory(memory_key='history', chat_memory=chat_history, k=8)

# Function to create a prompt template for the chat
def prompt_template(template):
    return PromptTemplate(template=template, input_variables=["history", "question"])

# Function to create a conversation chain with the given model, prompt, and memory
def llm_chain(llm, chat_prompt, memory):
    return ConversationChain(llm=llm, prompt=chat_prompt, memory=memory)

# Class to manage the chat chain process
class Chain:

    def __init__(self, chat_history) -> None:
        # Initialize memory, model, prompt, and chain
        self.memory = chat_memory(chat_history)
        self.llm = llm()
        self.prompt = prompt_template(template=memory_template)
        self.chain = llm_chain(self.llm, self.prompt, self.memory)

    # Method to run the chat chain with user input
    def invoke(self, user_input):
        return self.chain.invoke(input=user_input, history=self.memory.chat_memory.messages, stop=["AI"])
