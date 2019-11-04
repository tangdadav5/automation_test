# -*- coding: utf-8 -*-
from common.APP_KeyWord import KeyWord
import unittest
import time
import warnings


class TestCaselogin(unittest.TestCase,KeyWord):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽视各种ResourceWarning警告


    def test_case(self):
        """启动vskit"""
        self.dr = KeyWord()
        self.dr.wait(20)
        """点击登录"""
        self.dr.clickUiautomatorByName("Me") #点击Me按钮
        self.dr.clickUiautomatorByName("Log in")  # 点击login
        self.dr.clickUiautomatorByName("Email")  # 选择Email方式登陆
        self.dr.input_text_by_id("com.yomobigroup.chat:id/email_et","369@qq.com") #输入邮箱账号
        self.dr.clickUiautomatorByName("Next")  # 点击下一步
        self.dr.input_text_by_id("com.yomobigroup.chat:id/pwd_et", "qwerty")
        self.dr.clickUiautomatorByName("Next")  # 点击Email方式登陆
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()
