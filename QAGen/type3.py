
#
# https://python.langchain.com/docs/use_cases/question_answering/
# https://learn.deeplearning.ai/
#


#
# from langchain.document_loaders import TextLoader
import pandas
from langchain_community.document_loaders import JSONLoader

print("loader")
file = ("D:/project/langchain_community_study/QAGen/qa.json")



loader = JSONLoader(
    file_path=file,
    jq_schema='.messages[].content',
    text_content=False)

data = loader.load()




df = pandas.read_csv(file)
print(df.shape)
print(df.columns.tolist())

#
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("splits")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print(splits)

#
from langchain_community.embeddings.xinference import XinferenceEmbeddings
from langchain_community.vectorstores import Chroma

print("vectorstore")
embeddings = XinferenceEmbeddings(server_url="http://10.1.104.172:9997", model_uid="text2vec-base-chinese-sentence")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

#
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo', temperature=0.0)
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.chains.qa_generation.base import QAGenerationChain

print("RetrievalQA")
llm = ChatOllama(base_url="http://10.1.104.172:11434", model="gemma")
chain = QAGenerationChain.from_llm(llm, text_splitter=text_splitter)

qa = chain.run(docs)
print(chain)