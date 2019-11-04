# -*- coding: utf-8 -*-
import json
import hashlib
import random
from common.operation_yaml import Yaml
from config.config_path import *


class Common():
    """接口测试公用方法类"""

    def is_json_contain(self, result, expect, errmsg=''):
        """
        验证接口测试用例结果
        :Example    result={
                            "code":"000"
                            "name":"admin"，
                            "info":{"id":"1"，"phone":"12345645789"}}
                    expect={"name":"admin"}
        :param result:  实际结果
        :param expect:  预期结果
        :param errmsg:  错误信息
        :return:
        """
        if not isinstance(result, dict):
            errmsg += 'Fail,用例执行失败，原因：实际结果不是字典格式'
            return False, errmsg

        if not isinstance(expect, dict):
            errmsg += 'Fail,用例执行失败，原因：预期结果不是字典格式'
            return False, errmsg

        for key, value in expect.items():
            if key not in result:
                errmsg += "Fail,用例执行失败，原因：预期结果里面的key为{},不在实际结果里面".format(key)
                return False, errmsg

            # 预期结果和实际结果为字典
            elif isinstance(result[key], dict) and isinstance(expect[key], dict):
                re = self.is_json_contain(result[key], expect[key])
                if re is not True:
                    return re

            elif expect[key] != result[key]:
                errmsg += "Fail,用例执行失败，原因：key:{}对应的预期结果为:{};实际结果为:{}".format(key, expect[key], result[key])
                return False, errmsg

        return True, "PASS"

    def change_url(self, url):
        """
        读取excel中URL的参数化{url}，如果没有{url}，则执行url
        :param url: {url}
        :return: url
        """
        if '{' in url and url.startswith('{') and url.endswith('}'):  # 判断{ 在url中，并且以{ 开头，} 结束
            cfg = Yaml().read_yaml(read_yaml_path)  # 读取整个yaml文件
            new_name = url.split('{')[1].split('}')[0]  # 分离得到 apiurl 字段
            url = cfg[new_name]  # 读取yaml文件中的apiurl 并赋值给url参数
            return url
        else:
            return url

    def change_data(self, data):
        """
        处理请求入参，引用提取的变量
        :param data: 请求参数，并转换为dict格式
        :return: 入参
        """
        data = eval(data)  # 将str格式转换为python字典格式
        """如果入参中存在${xxx}，分离该获取xxx,并去yaml文件中找到xxx，并获取xxx的值"""
        for key, value in data.items():
            if value.startswith("$"):
                e = ((value.split("$")[1]).split("{")[1]).split("}")[0]  # 分离${topic_id}为 topic_id
                cfg = Yaml().read_yaml(write_yaml_path)[e]  # 获取topic_id
                data[e] = cfg  # 将${topic_id}替换为topic_id
        return data

    def changge_header(self, header):
        """
        处理头信息，如果不是字典转换为字典，如果为空添加一个默认请求头
        :param header: 请求头
        :return:
        """
        if header:
            if not isinstance(header, dict):
                header = eval(header)
                return header
        else:
            header = {"Content-Type": "application/x-www-form-urlencoded"}
            return header

    def md5(self, data):
        """
        md5加密方法
        :param data:  传入需要加密的参数
        :return:  加密后的参数
        """
        string = json.dumps(data)
        m = hashlib.md5()
        m.update(string.encode(encoding='utf-8'))
        return m.hexdigest()

    def generate_phone(self, top=None):
        """
        生成随机11位的电话号码
        :param top: 手机号段，可不填（默认随机）
        :return: 11位手机号码
        """
        if not top:
            phone_list = ["136","188","134","172","184","187"]    #定义号码段
            phone = random.choice(phone_list)+"".join(random.choice("0123456789") for _ in range(8))
        else:
            phone = str(top)+"".join(random.choice("0123456789") for _ in range(8))
        return phone


if __name__ == "__main__":
    print(Common().md5('123456'))
    print(Common().generate_phone(135))
