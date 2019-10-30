# -*- coding: utf-8 -*-
"""读取excel的sheet第二页用例"""
import unittest
import json
from ddt import ddt, data
from common.operation_excel import Excel
from common.HttpClient import HttpClientTest
from common.operation_yaml import Yaml
from common.common import Common
from config.config_path import *
from common.get_value_test import pop_list

excel = Excel(excel_path, 1)    # 实例化excel，并获取第二页的接口测试用例
@ddt
class ApiTestCase(unittest.TestCase, HttpClientTest, Common):
    """接口测试用例类"""
    data_list = excel.read_excel()  # 将获取的测试用例赋值给data_list，以便于DDT模块读取调用

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*data_list)
    def test_case(self, caseinfo):
        """接口测试用例"""
        rownum = self.data_list.index(caseinfo)  # 获取每列数据的索引
        url = self.change_url(caseinfo['url'])
        name = caseinfo["接口名"]
        methond = caseinfo['请求方法']
        header = eval(caseinfo['头信息'])
        data = self.change_data(caseinfo['入参'])
        result = caseinfo['断言']
        extract = caseinfo['提取变量']

        self.request(url + name, methond, result, data, headers=header, extract=extract, rownum=rownum)

    def request(self, url, methond, result, data=None, headers=None, extract=None, rownum=None):
        """发送请求方法"""

        res = HttpClientTest(url=url, methond=methond, data=data, headers=headers).run()   # 返回的是dict格式
        """提取响应值的变量，写入yaml文件中"""
        if extract:
            Yaml().write_yaml(write_yaml_path, (pop_list(res, extract)))# {提取值key: 提取方法(提取值value, 返回值)}

        """写入每个用例的响应值,openpyxl需要转换成str格式，rownum是索引，从0开始，openpyxl方法索引从1开始，实际表格第一行是标题，所以从第二行开始写入"""
        excel.write_excel(row=rownum+2, col=7, value=json.dumps(res))   # 写入excel中需要转换成字符串

        """转换预期结果为字典，获取字典的key,并切片成字符串格式"""
        keys = " ".join(json.loads(result).keys())  # 获取预期结果的key
        # print(keys)

        """拿预期结果key去获取实际结果相等的值，得到一个字典"""
        aaa = pop_list(res, keys)  # 拿预期结果key去获取实际结果相等的值
        # print(aaa)

        """预期结果与实际结果做对比，如果结果一致，将测试结果写入excel中"""
        re = Common().is_json_contain(aaa, json.loads(result))      # excel中的断言需要转换成字典格式
        excel.write_excel(row=rownum+2, col=10, value=re[1])
        self.assertTrue(re[0])


if __name__ == '__main__':
    unittest.main()

