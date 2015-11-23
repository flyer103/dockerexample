# 基础环境
FROM python
MAINTAINER flyer <flyer103@gmail.com>

# 复制代码
RUN mkdir /douban
COPY app.py requirements.txt /douban/
RUN pip3 install -r /douban/requirements.txt

# 对外服务端口
EXPOSE 9999

# 命令执行的目录
WORKDIR /douban

# 执行的命令
CMD ["python3", "app.py"]
