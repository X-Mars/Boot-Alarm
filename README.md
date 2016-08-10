# Boot-Alarm
## 用户登陆微信提醒
#### 安装部署   
```bash
yum install httpd -y  
git clone https://github.com/X-Mars/Boot-Alarm.git
cp Boot-Alarm/login.py /var/www/cgi-bin
chmod +x /var/www/cgi-bin/login.py
service httpd start
```
#### 触发链接
```bash
curl http://xxx.com/cgi-bin/login.py?SYSUSER=$USER\&LOCALIP=`ip addr|grep inet|grep -v 127.0.0.1 |awk '{print $2}' |awk -F / '{print $1}'`\&REMOTEIP=`last |grep still |grep $USER |head -1 |awk '{print $3}'`\&HOSTNAME=$HOSTNAME\&DATE=`date +%H:%M`
```
#### 添加触发链接到/etc/profile
```bash
echo "curl http://xxx.com/cgi-bin/login.py?SYSUSER=\$USER\&LOCALIP=\`ip addr|grep inet|grep -v 127.0.0.1 |awk '{print \$2}' |awk -F / '{print \$1}'\`\&REMOTEIP=\`last |grep still |grep \$USER |head -1 |awk '{print \$3}'\`\&HOSTNAME=\$HOSTNAME\&DATE=\`date +%H:%M\` >> /dev/null 2>&1" >> /etc/profile
