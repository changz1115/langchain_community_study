from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def main():
    model_local = ChatOllama(base_url="http://10.1.104.172:11434", model="gemma")
    template = "{topic}"
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model_local | StrOutputParser()
    print(chain.invoke("能详细说说maven都能干什么吗?"))

if __name__ == "__main__":
    main()
