
### 3.1 搭建本地LLM部署框架-Xinference


https://github.com/xorbitsai/inference

#### download anaconda:
https://www.anaconda.com/download#downloads

```shell
sh ./Anaconda3-2023.09-0-Linux-x86_64.sh -u
#conda config --set ssl_verify false
```

#### 这里需要确认g++以及make是否安装
```shell
conda create --name xinference python=3.10
conda activate xinference
#pip install "xinference[all]" -i https://mirror.baidu.com/pypi/simple
pip install "xinference[all]"
```

#### 如何需要安装++以及make
```shell
conda create --name xinference python=3.10
conda activate xinference

# python 编译器
# neusoftproxy
apt install g++
apt install make
export CXX=g++

# 花点时间
pip install --upgrade "xinference[all]" -i https://mirror.baidu.com/pypi/simple --trusted-host mirror.baidu.com
pip install "xinference[all]"

# 本机IP地址
xinference-local --host <本机IP地址> --port 9997
xinference-local --host 127.0.0.1 --port 9997
XINFERENCE_MODEL_SRC="modelscope" xinference-local --host localhost --port 9997

setx XINFERENCE_MODEL_SRC "modelscope"
xinference-local --host localhost --port 9997

HF_ENDPOINT=https://hf-mirror.com XINFERENCE_HOME=/usr/xinference xinference-local --host 10.1.104.172 --port 9997

```shell
(xinference) root@UASD-AIGC-172:~# xinference list -e http://10.1.104.172:9997
```

```test
UID           Type    Name          Format      Size (in billions)  Quantization
------------  ------  ------------  --------  --------------------  --------------
llama-2-chat  LLM     llama-2-chat  ggmlv3                       7  q2_K
chatglm       LLM     chatglm       ggmlv3                       6  q4_0
chatglm3      LLM     chatglm3      ggmlv3                       6  q4_0
UID                             Type       Name                              Dimensions
------------------------------  ---------  ------------------------------  ------------
text2vec-base-chinese-sentence  embedding  text2vec-base-chinese-sentence           768
```


## setup langchain_community

https://python.langchain.com/docs/use_cases/question_answering/sources

```shell
conda env list
conda activate xinference

pip install langchain
```

```shell
# 本机IP地址
xinference-local --host localhost --port 9997
HF_ENDPOINT=https://hf-mirror.com XINFERENCE_HOME=/usr/xinference xinference-local --host 10.1.104.172 --port 9997
```

