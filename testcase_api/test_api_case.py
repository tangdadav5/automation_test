# -*- coding: utf-8 -*-
import unittest
from common.HttpClient import HttpClientTest


class  ApiTestCase(unittest.TestCase,HttpClientTest):
    """API测试用例"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def testcase_get(self):
    #     """查询IP用例"""
    #     url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'
    #     data = {"query": "1.1.1.1",
    #             "resource_id": "6006"}
    #     response = HttpClientTest("GET", url, data).run()
    #     print(response)
    #
    # def testcase_post(self):
    #     """编辑帖子用例"""
    #     url = "http://39.107.96.138:3000/api/v1/topics/update"
    #     data = {"accesstoken" : "46c389c9-3cff-45cc-93f4-c3568558dc2a",
    #             "topic_id" : "5d8c752a839de20670141ac6",
    #             "title" : "这是编辑接口测试标题",
    #             "tab" : "job",
    #             "content" : "接口测试内容"}
    #     response = HttpClientTest("POST", url, json.dumps(data)).run()
    #     # 将respone返回值中的topic_id以字典形式存放在yaml文件中，以便后续case提取使用
    #     Yaml().write_yaml(write_yaml_path, {"topic_id": response["topic_id"]})
    #     # 读取yaml文件中的数据
    #     cfg = Yaml().read_yaml(write_yaml_path)["topic_id"]
    #     print("这是读取写入后的topic_id：", cfg)
    #     print(type(response), response)

    def test_zhjk(self):
        url = "http://222.212.141.46:8085/user/login"
        data = {"username": "gz0130", "password": "123"}
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        res = HttpClientTest("POST", url=url, data=data, headers=header).run()
        print(res)


if __name__ == "__main__":
    unittest.main()