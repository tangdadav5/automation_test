# -*- coding: utf-8 -*-
from appium import webdriver
from common.logger import Logger
from common.operation_yaml import Yaml
from config.config_path import chrome_path, read_yaml_path, ie_path, firefox_path

yaml = Yaml()
logger = Logger(logger='APP').getlog()


class AppiumDriver(object):

    def open_app(self):
        '''
        设置appium启动配置项
        :return: 返回appdriver实例
        '''
        cfg = yaml.read_yaml(read_yaml_path)
        desired_caps = {}
        desired_caps["platformName"] = cfg['platformName']
        desired_caps["platformVersion"] = cfg['platformVersion']
        desired_caps["deviceName"] = cfg['deviceName']
        desired_caps["appPackage"] = cfg['appPackage']
        desired_caps["appActivity"] = cfg['appActivity']
        desired_caps["unicodeKeyboard"] = cfg['unicodeKeyboard']
        desired_caps["resetKeyboard"] = cfg['resetKeyboard']
        desired_caps["noSign"] = cfg['noSign']
        desired_caps["noReset"] = cfg['noReset']
        desired_caps["device"] = cfg['device']
        desired_caps["autoGrantPermissions"] = cfg['autoGrantPermissions']

        # appremote_url=cfg['appremote_url']
        appdriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

        return appdriver


if __name__ == '__main__':
    appdriver = AppiumDriver()
    appdriver.open_app()
