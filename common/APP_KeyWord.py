# -*- coding: utf-8 -*-

from common.appiumdriver import AppiumDriver
from common.logger import Logger

logger = Logger(logger='KeyWord').getlog()


class KeyWord(AppiumDriver):
    """appium关键字封装类"""

    def __init__(self):
        """初始化appium配置"""
        self.appdriver = self.open_app()

    def close_app(self):
        """关闭浏览器"""
        self.appdriver.quit()
        logger.info('app关闭成功')

    def clickUiautomatorByName(self,name):
        """
        通过文本定位

        :param name: text元素值
        :return:
        """
        self.appdriver.find_element_by_android_uiautomator("new UiSelector().text(\"" + name + "\")").click()
        logger.info('{}元素点击成功'.format(name))

    def clickUiautomatorByResourceId(self,id):
        """
        通过文本定位

        :param name: text元素值
        :return:
        """
        self.appdriver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"" + id + "\")").click()
        logger.info('{}元素点击成功'.format(id))

    def input_text_by_id(self,id, text):
        """
        根据id输入文本内容
        :param text:
        :return:
        """
        element=self.appdriver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"" + id + "\")")
        element.send_keys(text)

    def wait(self, s):
        """隐示等待时间"""
        self.appdriver.implicitly_wait(s)
        logger.info('执行隐式等待，等待时长为{}秒'.format(s))

