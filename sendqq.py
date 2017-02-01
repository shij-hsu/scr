#!/usr/bin/env python
# coding=utf-8
import os,sys
import smtplib,time
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail():
	mailInfo={
	    "from":"wzwmxd@qq.com",
	    "to":"post8@gm-training.top",
	    "hostname":"smtp.qq.com",
	    "username":"wzwmxd",
	    "mailsubject":"title",
	    "mailencoding":"utf-8"
	}
	mailInfo['password']='odqgcwgbqeibebje'
	mailInfo['mailtext']="《薪酬管理高级班》及《离职管理中最棘手的100个问题》\n"
	smtp=SMTP_SSL(mailInfo["hostname"])
	smtp.set_debuglevel(0)
	smtp.ehlo(mailInfo["hostname"])
	smtp.login(mailInfo["username"],mailInfo["password"])

	msg=MIMEText(mailInfo["mailtext"],"plain",mailInfo["mailencoding"])
	msg['Subject']=Header(mailInfo['mailsubject'],mailInfo['mailencoding'])
	msg['from']=mailInfo['from']
	msg['to']=mailInfo['to']
	smtp.sendmail(mailInfo['from'],mailInfo['to'],msg.as_string())

	smtp.quit()
if __name__=='__main__':
	for i in range(1000):
		sendmail()
		print '\rsend email %d...'%i,
		time.sleep(1)

