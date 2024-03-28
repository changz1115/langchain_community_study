
import bs4

from langchain_community.llms import Xinference
from langchain_community.embeddings.xinference import XinferenceEmbeddings

from langchain_community.document_loaders import TextLoader
# from langchain_community.vectorstores import DocArrayInMemoRunnableParallelrySearch

from langchain import hub
from langchain_community.vectorstores import Chroma

# from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.runnables import RunnableParallel

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate



def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def main():

    print("1. 读取文件")
    # docs = TextLoader("d:/project/vscodeproject/langchain_community_study/RAG/三国演义白话文完整版.txt").load()
    bs_strainer = bs4.SoupStrainer(class_=("post-content", "post-title", "post-header"))
    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs={"parse_only": bs_strainer},
    )
    docs = loader.load()

    print("1.1 分词")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    print("2. 矢量并存储")
    print("2.1 矢量模型的使用")
    embeddings = XinferenceEmbeddings(server_url="http://10.1.104.172:9997", model_uid="text2vec-base-chinese-sentence")
    # embeddings = XinferenceEmbeddings(server_url="http://localhost:9997", model_uid="text2vec-base-chinese-sentence")
    print("2.2 vectorstore 矢量數據存储在memory DocArrayInMemorySearch")
    # vectorstore = DocArrayInMemorySearch.from_documents(splits, embeddings)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    print("2.3")
    retriever = vectorstore.as_retriever()
    print(retriever)

    print("3. 向主模型提问 定義格式")
    prompt = hub.pull("rlm/rag-prompt")

    print("主模型的使用")
    llm = Xinference(server_url="http://10.1.104.172:9997", model_uid="chatglm2")
    # llm = Xinference(server_url="http://localhost:9997", model_uid="chatglm2")
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    print("Q&A")
    print(rag_chain.invoke("What is Task Decomposition?"))

    print("Q&A with source")
    rag_chain_from_docs = (
        RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
        | prompt
        | llm
        | StrOutputParser()
    )
    rag_chain_with_source = RunnableParallel(
        {"context": retriever, "question": RunnablePassthrough()}
    ).assign(answer=rag_chain_from_docs)
    print(rag_chain_with_source.invoke("What is Task Decomposition"))

if __name__ == "__main__":
    main()