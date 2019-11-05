# -*- coding: utf-8 -*-
import unittest
import time
from common.HTMLTestRunner import HTMLTestRunner
from config.config_path import report_path
from common.sendmail import SendMail


def run():
    '''第一步：创建一个test suite实例'''
    testcases = unittest.TestSuite()

    '''第二步：用例集添加用例'''
    # 第一种，增加单个用例
    # testcases.addTest(TestCase1('test_case3'))
    # 第二种，增加多个用例
    # testcases.addTests([TestCase1('test_case3'),TestCase2('test_case3')])
    # 第三种，增加一个类的到用例集里，用TestLoader
    # testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase1))
    # testcases.addTests(unittest.TestLoader().loadTestsFromName('class_note.class18_report.TestCase1'))
    # testcases.addTests(unittest.TestLoader().loadTestsFromNames(['testcase.test_case.TestCase1', 'testcase.test_case.TestCase2']))

    testcases.addTests(unittest.TestLoader().loadTestsFromName('testcase_app.test_login.TestCaselogin'))

    '''第三步：TestTestRunner类里面的run方法执行'''
    # unittest.TextTestRunner().run(testcases)
    '''集成报告后的第三步'''
    report_name = "APP自动化测试报告"
    report_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    report_dir = report_path + report_name + report_time + ".html"
    with open(report_dir, 'wb') as file_path:
        runner = HTMLTestRunner(stream=file_path, title="APP自动化测试报告", description='Vskit邮箱登录模块', verbosity=2)
        runner.run(testcases)
    # SendMail().send_email()



if __name__ == '__main__':
    run()