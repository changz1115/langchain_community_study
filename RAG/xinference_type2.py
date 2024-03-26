from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.xinference import XinferenceEmbeddings
from langchain_community.llms import Xinference
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch

def main():
    model_local = Xinference(server_url="http://10.1.104.172:9997", model_uid="chatglm2")

    print("1. 读取文件并分词")
    documents = TextLoader("./三国演义白话文完整版.txt").load()
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    doc_splits = text_splitter.split_documents(documents)

    print("2. 嵌入并存储")
    print("2.1")
    embeddings = XinferenceEmbeddings(server_url="http://10.1.104.172:9997", model_uid="text2vec-base-chinese-sentence")
    print("2.2 vectorstore 矢量存储memory DocArrayInMemorySearch")
    vectorstore = DocArrayInMemorySearch.from_documents(doc_splits, embeddings)
    print("2.3")
    retriever = vectorstore.as_retriever()
    print(retriever)

    print("3. 向模型提问")
    template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model_local
        | StrOutputParser()
    )
    print(chain.invoke("身长七尺，细眼长髯的是谁？"))

if __name__ == "__main__":
    main()