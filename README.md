# Boot-Alarm
## 用户登陆微信提醒
### 微信企业号注册  
 * 注册微信企业号（团队类型） [点击注册](https://qy.weixin.qq.com/)    
   
#### 通讯录设置  
登陆微信企业号控制台  
点击左侧“通讯录”，新增部门（技术部）与子部门（运维部），并添加用户  
点击（运维部）后方的三角，修改部门，记录**部门ID**  
  
#### 创建应用  
点击左侧“应用中心”，新建消息型应用，应用名称为“zabbix报警”  
“应用可见范围”，添加刚刚新建的子部门（运维部）  
点击“zabbix报警”，记录**应用ID**
  
#### 应用权限设置  
点击左侧“设置”，权限管理，新建普通管理组，名称填写“zabbix报警组”  
点击修改“通讯录权限”，勾选（技术部）后方的管理  
点击修改“应用权限”，勾选刚刚创建的“zabbix报警”  
点击刚刚创建的“zabbix报警组”，记录左侧的**CorpID与Secret**
  
#### 收集微信相关信息
1. 记录**应用ID**
2. 记录**CorpID与Secret**
3. 记录**子部门（运维部）ID**
  
### 安装部署   
```bash
yum install httpd -y  
git clone https://github.com/X-Mars/Boot-Alarm.git
cp Boot-Alarm/login.py /var/www/cgi-bin
chmod +x /var/www/cgi-bin/login.py
service httpd start
```
### 触发链接
```bash
curl http://xxx.com/cgi-bin/login.py?SYSUSER=$USER\&LOCALIP=`ip addr|grep inet|grep -v 127.0.0.1 |awk '{print $2}' |awk -F / '{print $1}'`\&REMOTEIP=`last |grep still |grep $USER |head -1 |awk '{print $3}'`\&HOSTNAME=$HOSTNAME\&DATE=`date +%H:%M`
```
### 添加触发链接到/etc/profile
```bash
echo "curl http://xxx.com/cgi-bin/login.py?SYSUSER=\$USER\&LOCALIP=\`ip addr|grep inet|grep -v 127.0.0.1 |awk '{print \$2}' |awk -F / '{print \$1}'\`\&REMOTEIP=\`last |grep still |grep \$USER |head -1 |awk '{print \$3}'\`\&HOSTNAME=\$HOSTNAME\&DATE=\`date +%H:%M\` >> /dev/null 2>&1" >> /etc/profile
