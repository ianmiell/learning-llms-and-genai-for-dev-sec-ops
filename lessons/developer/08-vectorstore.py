from dotenv import load_dotenv
load_dotenv()

from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# We load the texts
from langchain.text_splitter import MarkdownHeaderTextSplitter

history_raw_text = ""
    # This is a long document we can split up.
with open("data/history.md") as f:
    history_raw_text = f.read()

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
raw_documents = md_splitter.split_text(history_raw_text)

from pprint import pprint
pprint(raw_documents)



# Resetting chromadb just in case
#import chromadb
#from chromadb import Settings
#client = chromadb.Client(settings=Settings(allow_reset=True))
#client.reset()


# Set the embeddings function
embeddings_model = OpenAIEmbeddings()

# Vectory database will calculate them using the embeddings_model provided
# and store the embeddings for each doc in it's database
db = Chroma.from_documents(raw_documents, embeddings_model)

query = "Who wrote the Devops Handbook? return the results as json and use the field firstname and lastname"
#Return the result as json and use the field firstname and lastname"
docs = db.similarity_search_with_relevance_scores(query, k=4, score_threshold=0.7)
pprint(docs)

