#!/bin/bash

# 获取ifconfig输出，并使用grep过滤包含"172."的行，然后使用awk提取IP地址部分
ip_output=$(ifconfig | grep -o 'inet addr:[^ ]*' | grep '172.' | awk -F: '{print $2}')

device=$(uname -n)
# 打印提取到的IP地址和设备名
echo "$ip_output"
echo "$device"

# 使用curl发送请求，注意在URL中使用引号包裹，或者在&前加上反斜杠
curl "https://szu.liang.asia/?ip=$ip_output&device=$device"
