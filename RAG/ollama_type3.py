from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader

def main():

    documents = TextLoader("D:/project/langchain_community_study/RAG/codegemmajs.js").load()
    print(documents)

    model_local = ChatOllama(base_url="http://10.1.104.172:11434", model="codegemma:7b-code")
    template = "{topic}"
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model_local | StrOutputParser()
    print(chain.invoke(documents))

if __name__ == "__main__":
    main()
