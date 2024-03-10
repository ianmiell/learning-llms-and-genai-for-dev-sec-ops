from dotenv import load_dotenv
load_dotenv()

from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

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

# Set the embeddings function
embeddings_model = OpenAIEmbeddings()

import chromadb

db = Chroma.from_documents(raw_documents, embeddings_model)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
from _lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler

pretty_print_callback = PrettyPrintCallbackHandler()
llm.callbacks = [pretty_print_callback]

qa_chain = RetrievalQA.from_chain_type(
    llm, retriever=db.as_retriever(), return_source_documents=True
)

query = "Who were the people involved in writing the devops Handbook ? If there are multiple authors return them all. Return the result as json and use the field firstname and lastname"

# First via the llm
from langchain.schema import (
    HumanMessage,
)

answer = llm([HumanMessage(content=query)])
pprint(answer)

# next via the llm via Retrieval Augmented Generation
answer = qa_chain({"query": query})
pprint(answer)
