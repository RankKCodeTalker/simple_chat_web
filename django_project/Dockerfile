# 从仓库拉取带有python3.6的Linux环境
FROM python:3.8

# 设置python环境变量
ENV PYTHONUNBUFFERED 1

# 创建pychatgpt文件夹并将其设置为工作目录
RUN mkdir /chat_davinci
WORKDIR /chat_davinci


# 设置pip清华源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 更新pip
RUN pip install pip -U

# 将requirements.txt复制到容器的pychatgpt目录
ADD requirements.txt /chat_davinci/

# 安装库
RUN pip install -r requirements.txt

# 将当前目录复制到容器的pychatgpt目录
ADD . /chat_davinci

CMD ["python3","manage.py","runserver","0.0.0.0:5000"]
