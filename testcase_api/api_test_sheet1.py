# -*- coding: utf-8 -*-

import unittest
import json
from ddt import ddt, data
from common.operation_excel import Excel
from common.HttpClient import HttpClientTest
from common.operation_yaml import Yaml
from common.common import Common
from config.config_path import *
from common.get_value import get_target_value

excel = Excel(excel_path, 0)


@ddt
class ApiTestCase(unittest.TestCase, HttpClientTest, Common):
    """接口测试用例类"""
    data_list = excel.read_excel()

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


        """调用发送请求方法"""
        if methond == 'get':
            self.request(url + name, methond, result, data, headers=header, extract=extract, rownum=rownum)
        elif methond == 'post':
            self.request(url + name, methond, result, json.dumps(data), headers=header, extract=extract, rownum=rownum) # 将data转换为str格式发送请求


    def request(self, url, methond, result, data=None, headers=None, extract=None, rownum=None):
        """发送请求方法"""

        res = HttpClientTest(url=url, methond=methond, data=data, headers=headers).run()   # 返回的是dict格式

        """提取响应值的变量，写入yaml文件中"""
        if extract:
           # Yaml().write_yaml(write_yaml_path, {extract: res[extract]})
           Yaml().write_yaml(write_yaml_path, {extract: get_target_value(extract, res)})

        """写入每个用例的响应值,openpyxl需要转换成str格式，rownum是索引，从0开始，openpyxl方法索引从1开始，实际表格第一行是标题，所以从第二行开始写入"""
        excel.write_excel(row=rownum+2, col=7, value=json.dumps(res))   # 写入excel中需要转换成字符串

        """预期结果与实际结果一致，将测试结果写入excel中"""
        re = Common().is_json_contain(res, json.loads(result))      # excel中的断言需要转换成字典格式
        excel.write_excel(row=rownum+2, col=10, value=re[1])
        self.assertTrue(re[0])


if __name__ == '__main__':
    unittest.main()

