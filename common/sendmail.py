# -*- coding: utf-8 -*-
import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.config_path import report_path
from config.config import ConfigParser


class SendMail():
    """发送邮件"""
    def send_email(self):
        """文件路劲转换内容的HTML邮件"""
        # 获取最新报告
        lists = os.listdir(report_path)
        file = os.path.join(report_path, lists[-1])

        # 创建HTML内容
        htmlfile = open(file, 'r+', encoding='utf-8')
        htmldata = htmlfile.read()
        htmlfile.close()
        content = MIMEText(htmldata, 'html', 'utf-8')  # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码

        # 构造邮件附件
        fail = MIMEApplication(open(file, 'rb').read())
        fail["Content-Type"] = 'application/octet-stream'
        fail.add_header('Content-Disposition', 'attachment', filename="TestReport.html")  # 邮件格式以及附件标题

        # 创建一个带附件的实例
        msg = MIMEMultipart()

        # 读取配置文件内容
        conf = ConfigParser()
        sender = conf.get_config("email", "sender")
        pwd = conf.get_config("email", "password")
        port = conf.get_config("email", "port")
        smtp_server = conf.get_config("email", "smtp")
        receiver = conf.get_config("email", "receiver")

        # 添加邮件头
        msg['subject'] = Header(u'自动化测试结果', 'utf-8')      # 邮件标题
        msg['from'] = sender                                    # 邮件发送人
        msg['to'] = receiver                                    # 邮件接收人
        password = pwd                                          # 邮件发送人密码

        # 添加邮件发送内容
        msg.attach(content)     # 邮件内容
        msg.attach(fail)        # 邮件附件

        # 发送邮件
        try:
            server = smtplib.SMTP(smtp_server, port)  # SMTP协议默认端口是25
            server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息。
            server.login(msg['from'], password)  # 登录邮箱
            server.sendmail(msg['from'], msg['to'], msg.as_string())  # 邮件正文是一个str，as_string()把MIMEText对象变成str。
            server.quit()
            print('邮件发送成功')
        except (Exception):
            print("Err:邮件发送失败....")


if __name__ == "__main__":
    SendMail().send_email()
