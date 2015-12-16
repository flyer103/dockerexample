### 使用说明
#### 使用 python
$ docker run --rm -v 本地PYTHON目录:/data/ flyer103/python3.5 本地PYTHON目录/PYTHON文件

#### 安装包
$ docker run --rm -v 本地VOLUME目录:/data/py-pkg/ flyer103/python3.5 pip install PYTHON包

#### 使用包
假设安装了 requests 包:
$ docker run --rm -v 本地VOLUME目录:/data/py-pkg/ flyer103/python3.5 python -c "import requests; print(requests.get('http://www.baixing.com'))"

#### PYTHON 包包含可执行命令
假设安装了 ipython:
$ docker run --rm -it -v 本地VOLUME目录:/data/py-pkg/ flyer103/python3.5 ipython