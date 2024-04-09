


from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

# from langchain_community.llms import Xinference
from langchain_community.embeddings.xinference import XinferenceEmbeddings
from langchain_community.chat_models import ChatOllama
# from langchain_community.chat_models import OllamaEmbeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.runnables import RunnableParallel

print("loader")
# file = ("D:/project/langchain_community_study/QAGen/develop_txt.pdf")
file = ("/home/changzheng/文档/project/vscode/langchain_community_study/QAGen/develop_txt.pdf")
loader = PyPDFLoader(file_path=file)
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print("vectorstore")
<<<<<<< HEAD
embeddings = XinferenceEmbeddings(server_url="http://10.1.104.172:9997", model_uid="text2vec-base-chinese-sentence")
# embeddings = XinferenceEmbeddings(server_url="http://127.0.0.1:9997", model_uid="text2vec-large-chinese")
=======
embeddings = XinferenceEmbeddings(server_url="http://127.0.0.1:9997", model_uid="text2vec-base-chinese")
>>>>>>> 1fc3d6b (	修改：     QAGen/type2.py)
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

<<<<<<< HEAD
llm = ChatOllama(base_url="http://10.1.104.172:11434", model="gemma")
# llm = Xinference(server_url="http://10.1.104.172:9997", model_uid="gemma-it")
=======
# llm = ChatOllama(base_url="http://10.1.104.172:11434", model="gemma")
llm = Xinference(server_url="http://127.0.0.1:9997", model_uid="gemma-it")
>>>>>>> 1fc3d6b (	修改：     QAGen/type2.py)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

q = "能详细说说maven都能干什么吗?"
print(q)
rag_chain_from_docs = (
    RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
    | prompt
    | llm
    | StrOutputParser()
)
rag_chain_with_source = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
).assign(answer=rag_chain_from_docs)

print(rag_chain_with_source.invoke(q))