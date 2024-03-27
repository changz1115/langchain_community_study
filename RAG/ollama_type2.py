
import bs4

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_community import embeddings
from langchain_community.embeddings.xinference import XinferenceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.embeddings import OllamaEmbeddings

def main():
    model_local = ChatOllama(base_url="http://10.1.104.172:11434", model="llava")

    print("1. 读取文件并分词")
    documents = TextLoader("D:/project/langchain_community_study/RAG/file_return_code.txt").load()
    # bs_strainer = bs4.SoupStrainer(class_=("post-content", "post-title", "post-header"))
    # loader = WebBaseLoader(
    #     web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    #     bs_kwargs={"parse_only": bs_strainer},
    # )
    # documents = loader.load()

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    doc_splits = text_splitter.split_documents(documents)

    print("2. 嵌入并存储")
    print("2.1")
    # embeddings = OllamaEmbeddings(base_url="http://10.1.104.172:11434", model="nomic-embed-text")
    embeddings = XinferenceEmbeddings(server_url="http://10.1.104.172:9997", model_uid="text2vec-base-chinese-sentence")
    print("2.2")
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
    print(chain.invoke("高位数字为4,低位数字为3的时候,什么意思?"))

if __name__ == "__main__":
    main()