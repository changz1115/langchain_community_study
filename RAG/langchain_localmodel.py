# https://python.langchain.com/docs/use_cases/question_answering/local_retrieval_qa

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# load input文档 这里是https协议的一个网站
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

# 分词 split 把文章分成若干块 检索的时候会以块为单位
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

print(all_splits)

from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())