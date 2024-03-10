from dotenv import load_dotenv
load_dotenv()

history_raw_text = ""
# This is a long document we can split up.
with open("data/history.md") as f:
    history_raw_text = f.read()

# naive , generic chunksize splitter

from langchain.text_splitter import RecursiveCharacterTextSplitter

# Set a really small chunk size, just to show.
text_splitter = RecursiveCharacterTextSplitter(
     chunk_size=100,
     chunk_overlap=0,
     length_function=len,
     add_start_index=True,
)
texts = text_splitter.create_documents([history_raw_text])

from pprint import pprint
pprint(texts)



# Now use a document/content specific splitter
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
texts = md_splitter.split_text(history_raw_text)

pprint(texts)

