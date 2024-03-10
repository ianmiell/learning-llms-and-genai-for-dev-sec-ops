from dotenv import load_dotenv
load_dotenv()
# Initialize a chat model instead of a regular LLM
from langchain_openai import ChatOpenAI
chat = ChatOpenAI()



from langchain.schema import (
    SystemMessage,
    AIMessage,
    HumanMessage
)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
answer = chat(messages)
print(answer)

#from lessons._lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler
from _lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler

pretty_print_callback = PrettyPrintCallbackHandler()

chat = ChatOpenAI(callbacks=[pretty_print_callback])
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
answer = chat(messages)


