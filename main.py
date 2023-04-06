from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import apiKey
import os
os.environ["OPENAI_API_KEY"] = apiKey.apiKey
from langchain.document_loaders import TextLoader
loader = TextLoader('aristotle.txt')
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
 query = input()
##index.query(query)
 print(index.query_with_sources(query))
 