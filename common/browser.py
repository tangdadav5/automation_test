# -*- coding: utf-8 -*-
from selenium import webdriver
from common.logger import Logger
from common.operation_yaml import Yaml
from config.config_path import chrome_path, read_yaml_path, ie_path, firefox_path

yaml = Yaml()
logger = Logger(logger='Browser').getlog()


class Browser(object):

    def open_browser(self):
        '''
        设置浏览器属性
        :return: 返回浏览器实例
        '''
        cfg = yaml.read_yaml(read_yaml_path)            # normal 浏览器正常模式
        if cfg['browser']['type'] == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument('headless')                  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            options.add_argument('start-maximized')           # 最大化浏览器
            options.add_argument('disable-infobars')          # 去除浏览器黄条警告
            options.add_argument('disable-extensions')        # 禁用浏览器扩展
            options.add_argument('disable-popup-blocking')    # 禁止弹出拦截信息
            options.add_argument('disable-gpu')               # 规避chrome浏览器bug
            browser = webdriver.Chrome(options=options,executable_path=chrome_path)
            logger.info('启动Chrome浏览器')
        elif cfg['browser']['type'] == 'ie':
            browser = webdriver.Ie(executable_path=ie_path)
        elif cfg['browser']['type'] == 'firefox':
            browser = webdriver.Firefox(executable_path=firefox_path)
        else:
            raise ('浏览器类型错误，请检查浏览器属性')
        # browser.get(url)
        # browser.get(cfg['url'])
        # logger.info('打开的URL为:{}'.format(cfg['ketangurl']))
        return browser


if __name__ == '__main__':
    browser = Browser()
    browser.open_browser()
