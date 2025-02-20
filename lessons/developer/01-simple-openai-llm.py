#pip install langchain-community openai python-dotenv langchain unstructured markdown tiktoken chromadb google-search-results langchain-openai crewai duckduckgo-search

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI
llm = OpenAI()
answer = llm("Hello world")
print(answer)

llm = OpenAI()
for i in range(1,6):
    answer = llm("Hello world")
    print(f"A{i}:{answer}")

llm = OpenAI(temperature=0)
for i in range(1,6):
    answer = llm("Hello world")
    print(f"A{i}:{answer}")

llm = OpenAI(streaming=True, temperature=0)
answer=llm("Where in the world is Brussels? try to answer verbose")
print(answer)

print(f"Context Size: {OpenAI().max_context_size}")
print(f"Max Tokens :{OpenAI().max_tokens}")

