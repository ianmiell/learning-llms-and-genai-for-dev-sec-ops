from dotenv import load_dotenv
load_dotenv()
import langchain_openai
from langchain_openai import OpenAI


# Enable global debugging
langchain_openai.debug = True

llm = OpenAI(temperature=0)
llm("Hello world")
langchain_openai.debug = False



# Set verbose flag on objects
llm = OpenAI(verbose=True, temperature=0)
llm("Hello World")


# Use a callback handler
from _lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler

callback = PrettyPrintCallbackHandler()
llm = OpenAI(streaming=True, temperature=0 , callbacks=[callback])
llm("Hello world")

