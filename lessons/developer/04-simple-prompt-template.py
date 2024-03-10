from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt = prompt_template.format(adjective="funny", content="chickens")

from langchain_openai import OpenAI
llm = OpenAI(temperature=0)
llm(prompt=prompt)

from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI bot. Your name is {name}."),
    ("human", "Hello, how are you doing?"),
    ("ai", "I'm doing well, thanks!"),
    ("human", "{user_input}"),
])

messages = template.format_messages(
    name="Bob",
    user_input="What is your name?"
)

#from lessons._lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler
from _lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler

pretty_print_callback = PrettyPrintCallbackHandler()

from langchain_openai import ChatOpenAI
chat = ChatOpenAI(temperature=0, callbacks=[pretty_print_callback])
chat(messages=messages)

