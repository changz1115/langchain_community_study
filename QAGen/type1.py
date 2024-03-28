

# from langchain.chains.qa_generation.base import QAGenerationChain

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file = ("D:/project/langchain_community_study/QAGen/develop_txt.pdf")
loader = PyPDFLoader(file_path=file)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

from langchain_community.embeddings.xinference import XinferenceEmbeddings
from langchain_community.vectorstores import Chroma


embeddings = XinferenceEmbeddings(server_url="http://10.1.104.172:9997", model_uid="text2vec-base-chinese-sentence")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# print("vectorstore.similarity_search 什么是maven?")
# docs = vectorstore.similarity_search("什么是maven?", k=3)
# for doc in docs:
#     print(str(doc.metadata["page"]) + ":?????", doc.page_content[:300])



from langchain import hub
from langchain_community.llms import Xinference
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

retriever = vectorstore.as_retriever()

prompt = hub.pull("rlm/rag-prompt")
llm = Xinference(server_url="http://10.1.104.172:9997", model_uid="chatglm2")

format_docs = "\n\n".join(doc.page_content for doc in docs)
print(format_docs)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
print("rag_chain.invoke 什么是maven?")
print(rag_chain.invoke("什么是maven?"))