
# setup langchain_community

```shell
conda env list
conda activate xinference

pip install langchain
```

```shell
# 本机IP地址
xinference-local --host <本机IP地址> --port 9997
xinference-local --host 127.0.0.1 --port 9997
xinference-local --host localhost --port 9997
HF_ENDPOINT=https://hf-mirror.com XINFERENCE_HOME=/usr/xinference xinference-local --host 10.1.104.172 --port 9997
```