#!/usr/bin/python
#_*_coding:utf-8 _*_
#作者:火星小刘 email：xtlyk@163.com


import cgi
import urllib,urllib2
import json
import sys
import simplejson

print "Content-type: text/html\n"
form = cgi.FieldStorage()

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    print  gettoken_url
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
 
 
def senddata(access_token,user,subject,content):
 
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":user,    #企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        "toparty":"4",    #企业号中的部门id。
        "msgtype":"text", #消息类型。
        "agentid":"5",    #企业号中的应用id。
        "text":{
            "content":subject + '\n' + content
           },
        "safe":"0"
        }
#    send_data = json.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_data = simplejson.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)
 
 
if __name__ == '__main__':

    user = "angrymars"
    content = "用户名:" + form["SYSUSER"].value + '\n' + "本地ip:" + form["LOCALIP"].value + '\n' + "登陆ip:" + form["REMOTEIP"].value + '\n' + "时间:" + form["DATE"].value
    subject = form["HOSTNAME"].value + "有用户登陆"
    
    corpid =  'wx5d8053'
    corpsecret = 'FOPk4InFkXaAvHFdz6-_NjeZ9gHN1zJG'
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,user,subject,content)
