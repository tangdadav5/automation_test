# -*- coding: utf-8 -*-
import requests
import json


default_headers = {
    "Content-Type":"application/json"
}


class HttpClientTest():
    """备份HttpClient类"""
    def __init__(self, methond, url, data=None, headers=None, files=None):
        if headers:
            for key, value in headers.items():
                default_headers[key] = value
        self.methond = methond
        self.url = url
        self.data = data
        self.files = files

    def send_get(self):
        """GET请求"""
        res = requests.get(url=self.url, params=self.data, headers=default_headers)
        return res.json()

    def send_post(self):
        """POST请求"""
        res = requests.post(url=self.url, data=self.data, headers=default_headers)
        return res.json()

    def run(self):
        """运行方法"""
        if self.methond.upper() == 'GET':
            res = self.send_get()
        elif self.methond.upper() == 'POST':
            res = self.send_post()
        else:
            res = {}
        return res


if __name__ == '__main__':
    get_url = 'http://39.107.96.138:3000/api/v1/topics'
    get_data = {"page": "1", "tab": "share", "limit": "2"}
    headers = {}
    response1 = HttpClientTest("get", get_url, get_data, headers).run()
    print('获取结果',type(response1),response1)
    print('success:', response1['data'][0]['tab'])
    print('------------------------------------------------------')

    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'
    data = {"query": "1.1.1.1","resource_id": "6006"}
    res = HttpClientTest("GET", url, data).run()
    print('获取结果',type(res),res)
    print('status:',res['status'])
    print('------------------------------------------------------')

    post_url = "http://39.107.96.138:3000/api/v1/topics/update"
    post_data = {"accesstoken" : "279a2502-f275-405d-9983-e43933159324",
            "topic_id" : "5d7e5856f68ffe76db4b7873",
            "title" : "这是编辑接口测试标题",
            "tab" : "job",
            "content" : "接口测试内容"}
    response = HttpClientTest('post', post_url, data=json.dumps(post_data)).run()
    print('获取结果',type(response),response)
    print('success:', response['success'])
