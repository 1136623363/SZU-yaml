from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    # 获取请求参数中的 IP 地址
    ip_address = request.args.get('ip')

    device_name = request.args.get('device')

    # 打印 IP 地址到控制台
    print(f"Received IP Address: {ip_address}")

    # 返回响应
    return f"Received IP Address: {ip_address}"

if __name__ == '__main__':
    # 启动 Flask 应用在指定的主机和端口
    app.run(host='192.168.31.22', port=9099)
