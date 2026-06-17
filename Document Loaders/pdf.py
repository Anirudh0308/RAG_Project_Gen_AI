from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("Document Loaders/GRU.pdf")

docs = data.load()

print(docs[14])
