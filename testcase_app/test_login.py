# -*- coding: utf-8 -*-
from common.APP_KeyWord import KeyWord
import unittest
import time
import warnings
from selenium.webdriver.common.by import By

class TestCaselogin(unittest.TestCase,KeyWord):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽视各种ResourceWarning警告


    def test_case(self):
        """启动vskit"""
        self.dr = KeyWord()
        time.sleep(10)
        """点击登录"""
        # self.dr.click_by_name("Me")
        # self.dr.wait_element( "com.xxx.xxx.ceshi:id/main_select_index_rb", "没有发现xxxx...")
        print("开始测试")
        self.dr.clickUiautomatorByName("Me") #点击Me按钮
        self.dr.clickUiautomatorByName("Log in")  # 点击login
        self.dr.click_by_id("com.yomobigroup.chat:id/email")  # 选择Email方式登陆
        self.dr.input_text_by_id("com.yomobigroup.chat:id/email_et","369@qq.com") #输入邮箱账号
        self.dr.clickUiautomatorByName("Next")  # 点击下一步
        self.dr.input_text_by_id("com.yomobigroup.chat:id/pwd_et", "qwerty")
        actual_text=self.dr.get_text_byid("com.yomobigroup.chat:id/email_forget_pwd")
        print(actual_text)
        self.assertEqual(actual_text,"Forget password?")
        print("测试结束")

if __name__ == "__main__":
    unittest.main()
