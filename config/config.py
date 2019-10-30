# -*- coding: utf-8 -*-
import configparser
import os

# 用os模块来读取
curpath = os.path.dirname(os.path.abspath(__file__))
ini_path = os.path.join(curpath, "config.ini")  # 读取到本机的配置文件路径

class ConfigParser():

    def get_config(self, sector, option):
        """
        获取配置文件得value
        :param sector:
        :param option: key
        :return: value
        """
        conf = configparser.ConfigParser()
        conf.read(ini_path, encoding='utf8')
        value = conf.get(sector, option)
        return value


if __name__ == '__main__':
    con = ConfigParser()
    res = con.get_config('email', 'receiver')
    print(res)