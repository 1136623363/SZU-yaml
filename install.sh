#执行代码wget -O install.sh https://szu.liang.asia/install.sh && bash install.sh

wget -O device_ip.sh https://szu.liang.asia/device_ip.sh

mv device_ip.sh /etc/storage/device_ip.sh
chmod +x /etc/storage/device_ip.sh
bash /etc/storage/device_ip.sh
echo '/etc/storage/device_ip.sh' >> /etc/storage/post_wan_script.sh
sed -i '/# 基本格式 : /a\10 */1 * * * /etc/storage/device_ip.sh' "/etc/storage/crontabs_script.sh"