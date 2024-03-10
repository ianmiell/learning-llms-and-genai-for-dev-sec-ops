from dotenv import load_dotenv
load_dotenv()

from _lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler
pretty_callback = PrettyPrintCallbackHandler()

from langchain_openai import OpenAI
llm = OpenAI(temperature=0, callbacks=[pretty_callback])

from langchain.chains.api import open_meteo_docs
from langchain.chains import APIChain
chain = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS,limit_to_domains=('https://api.open-meteo.com',))

chain.run('What is the weather like right now in London in degrees Celcius?')

