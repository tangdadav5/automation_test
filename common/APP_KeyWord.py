# -*- coding: utf-8 -*-

from common.appiumdriver import AppiumDriver
from common.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest
import os
import socket
from config.config_path import picture_path

logger = Logger(logger='KeyWord').getlog()


class KeyWord(AppiumDriver):
    """appium关键字封装类"""

    def __init__(self):
        """初始化appium配置"""
        self.run_appium_services("appium -a 127.0.0.1 -p 4723 --command-timeout 600")
        time.sleep(30)
        self.appdriver = self.open_app()


    def close_app(self):
        """关闭浏览器"""
        self.appdriver.quit()
        logger.info('app关闭成功')

    def is_port_used(self,ip, port):
        """
        check whether the port is used by other program
        检测端口是否被占用

        :param ip:
        :param port:
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False



    def run_appium_services(self,cmd):
        res=self.is_port_used("127.0.0.1",4723)
        if(res):
            logger.info("appium服务4723端口已经启动，无须重复启动")
        else:
            os.system(cmd)
            logger.info("appium服务已启动")



    def clickUiautomatorByName(self,name):
        """
        通过文本定位(显示等待)

        :param name: text元素值
        :return:
        """
        try:
            element = WebDriverWait(self.appdriver, 10).until(
                lambda driver: driver.find_element_by_android_uiautomator("new UiSelector().text(\"" + name + "\")"))
            element.click()
            # self.appdriver.find_element_by_android_uiautomator("new UiSelector().text(\"" + name + "\")").click()
            logger.info('执行元素等待出现并进行点击操作成功，元素值为：{}'.format(name))
        except:
            self.get_shot()
            logger.error('执行元素等待失败！！！，定位方法以及元素为：{} '.format(name))
            # raise ('执行元素等待失败！！！，定位方法以及元素为：{} '.format(name))


    def clickUiautomatorById(self,id):
        """
        通过uiautomator   id定位

        :param name: id
        :return:
        """
        try:
            element = WebDriverWait(self.appdriver, 10).until(
                lambda driver: driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"" + id + "\")"))
            element.click()
            # self.appdriver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"" + id + "\")").click()
            logger.info('执行元素等待出现并进行点击操作成功，元素值为：{}'.format(id))
        except:
            self.get_shot()
            logger.error('执行元素等待失败！！！，定位方法以及元素为：{} '.format(id))
            # raise ('执行元素等待失败！！！，定位方法以及元素为：{} '.format(id))


    def click_by_name(self,name):
        """
        通过文本定位点击，1.5.0版本以后的appium不支持(废弃)

        :param name: text元素值
        :return:
        """
        self.appdriver.find_element_by_name(name).click()
        logger.info('{}元素点击成功'.format(name))


    def click_by_id(self,id):
        """
        根据id点击
        :param id:
        :return:
        """
        try:
            WebDriverWait(self.appdriver, 10).until(EC.presence_of_element_located((By.ID, id))).click()
            logger.info('执行元素等待出现并进行点击操作成功，元素值为：{}'.format(id))
        except:
            self.get_shot()
            logger.error('执行元素等待失败！！！，定位方法以及元素为：{} '.format(id))
            # raise ('执行元素等待失败！！！，定位方法以及元素为：{} '.format(id))
        # self.appdriver.find_element_by_id(id).click()


    def input_text_by_uiauto_id(self,id, text):
        """
        根据id输入文本内容
        :param text:
        :return:
        """
        element=self.appdriver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"" + id + "\")")
        element.send_keys(text)


    def input_text_by_id(self,id, text):
        """
        根据id输入文本内容(推荐)
        :param text:
        :return:
        """
        try:
            # self.appdriver.find_element_by_id(id).send_keys(text)
            WebDriverWait(self.appdriver, 10).until(EC.presence_of_element_located((By.ID, id))).send_keys(text)
            logger.info('执行元素等待出现并输入文本信息{}，元素值为：{}'.format(text,id))
        except:
            logger.error('执行元素等待失败！！！{}输入失败，定位方法以及元素为：{} '.format(text,id))
            self.get_shot()


    def wait(self, s):
        """隐示等待时间"""
        self.appdriver.implicitly_wait(s)
        logger.info('执行隐式等待，等待时长为{}秒'.format(s))


    def element_wait__click(self, locator):
        '''
        等待元素出现，并进行点击操作
        :param locator:  定位方法
        :return:
        '''

        try:
            element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            element.click()
            logger.info('执行元素等待出现并进行点击操作成功，元素值为：{}'.format(locator))
        except:
            self.get_shot()
            logger.error('执行元素等待失败！！！，定位方法以及元素为：{} '.format(locator))
            raise ('执行元素等待失败！！！，定位方法以及元素为：{} '.format(locator))


    def get_shot(self):
        """
        运行异常进行截图操作
        :return:
        """
        picture_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        try:
            self.appdriver.get_screenshot_as_file(picture_path + picture_time + '.png')
            logger.info('错误信息已截图，截图地址为：{}'.format(picture_path + picture_time + '.png'))
        except:
            logger.error("执行截图操作失败！！！")
            raise ("执行截图操作失败！！！")


    #获取文本信息
    def get_text_byid(self,id):
        actual_text=self.appdriver.find_element_by_id(id).text
        return actual_text





