from flask import Flask, request,send_file

app = Flask(__name__)

CONFIG_FILE = 'szu.yaml'

import yaml

def update(ip_address, device_name):
    # 读取yaml文件
    with open('szu.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    # 遍历proxies列表，根据device_name更新或添加对应的条目
    updated = False
    for proxy in data.get('proxies', []):
        if proxy.get('name') == device_name:
            proxy['server'] = ip_address
            updated = True
            break

    # 如果proxies中没有对应的device_name，则新建一个条目
    if not updated:
        new_proxy = {
            'cipher': 'aes-256-cfb',
            'name': device_name,
            'password': '1234567890',  # 你可能需要根据实际情况更改密码等信息
            'port': 8388,
            'server': ip_address,
            'type': 'ss',
            'udp': True
        }
        data.setdefault('proxies', []).append(new_proxy)

    # 将更新后的数据写回yaml文件
    with open('szu.yaml', 'w') as file:
        yaml.dump(data, file)


@app.route('/szu', methods=['GET'])
def download_test_yaml():
    # 指定 szu.yaml 文件的路径
    file_path = './szu.yaml'

    # 使用 Flask 提供的 send_file 函数发送文件
    return send_file(file_path, as_attachment=True)

@app.route('/', methods=['GET'])
def get_ip():
    # 获取请求参数中的 IP 地址和设备名称
    ip_address = request.args.get('ip')
    device_name = request.args.get('device')

    # 打印 IP 地址到控制台
    print(f"Received IP Address: {ip_address} \n Received device_name:{device_name}")
    # 示例调用
    if ip_address:
        update(ip_address, device_name)

    # 返回响应
    return f"Received IP Address: {ip_address} \n Received device_name:{device_name}"

if __name__ == '__main__':
    # 启动 Flask 应用在指定的主机和端口
    app.run(host='0.0.0.0', port=9099)
