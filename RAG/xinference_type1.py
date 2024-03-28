from langchain_community.llms import Xinference
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def main():
    llm = Xinference(
        server_url="http://10.1.104.172:9997", model_uid="chatglm2"
    )

    # llm(
    #     prompt="Q: where can we visit in the capital of France? A:",
    #     generate_config={"max_tokens": 1024, "stream": True},
    # )

    template = "{topic}"
    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    generated = llm_chain.run("能详细说说maven都能干什么吗?")
    print(generated)

if __name__ == "__main__":
    main()
