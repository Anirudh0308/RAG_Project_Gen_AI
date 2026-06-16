from langchain_community.document_loaders import TextLoader

data = TextLoader("Document Loaders/notes.txt")
# data = TextLoader( r"D:\RAG Project\Document Loaders\notes.txt")

docs = data.load()

print(docs)
