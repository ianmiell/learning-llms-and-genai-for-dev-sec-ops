from dotenv import load_dotenv
load_dotenv()

# Load a doc as text file
from langchain_community.document_loaders import TextLoader

loader = TextLoader("./data/history.md")
loader.load()

#pip install unstructured markdown

from langchain_community.document_loaders import UnstructuredMarkdownLoader
loader = UnstructuredMarkdownLoader("./data/history.md")
loader.load()

from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    "./",
    glob="data/**/*.*",
    use_multithreading=True,
    max_concurrency=4,
    show_progress=True,
)
loader.load()


# https://python.langchain.com/docs/integrations/document_loaders/web_base
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://jedi.be")

data = loader.load()
print(data)


