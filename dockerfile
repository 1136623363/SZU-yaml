# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装应用所需的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用的端口
EXPOSE 9099

# 定义容器启动时运行的命令
CMD ["python", "app.py"]
