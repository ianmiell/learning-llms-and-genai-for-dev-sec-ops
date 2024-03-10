# Install the necessary packages - tiktoken is used for calculating tokens
from dotenv import load_dotenv
load_dotenv()

# https://python.langchain.com/docs/modules/data_connection/text_embedding/

from dotenv import load_dotenv
load_dotenv()
from langchain_openai.embeddings import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings()

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print(f"Embeddings calculated: {len(embeddings)}")
print(f"Vectorsize of first embedding :{len(embeddings[0])}")


# calculate the embedding of the query
embedded_query_results = embeddings_model.embed_query("What was the name mentioned in the conversation?")
print(f"Vectorsize of query text embedding :{len(embedded_query_results)}")

