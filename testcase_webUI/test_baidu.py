# -*- coding: utf-8 -*-
from common.pyselenium import KeyWord
from pagas.baidu_page import Baidu_search
import unittest


class TestCaseBaidu(unittest.TestCase,KeyWord):
    """百度搜索测试"""
    @classmethod
    def setUpClass(self):
        """打开浏览器"""
        self.driver = KeyWord()
        self.driver.get("https://www.baidu.com/")
        self.driver.wait(10)


    def test_case1(self):
        """搜索123"""

        self.driver.element_until_send_keys(Baidu_search.send_keys,'123')
        self.driver.element_until_click(Baidu_search.click)
        self.driver.get_text(Baidu_search.text)



    @classmethod
    def tearDownClass(self):
        """关闭浏览器"""
        self.driver.close_browser()


if __name__ == "__main__":
    unittest.main()
