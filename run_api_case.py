# -*- coding: utf-8 -*-
import unittest
import time
from common.HTMLTestRunner import HTMLTestRunner
from config.config_path import report_path
# from common.sendmail import SendMail


def run():
    testcases = unittest.TestSuite()
    testcases.addTests(unittest.TestLoader().loadTestsFromName('testcase_api.test_api.ApiTestCase'))
    report_name = "API自动化测试报告"
    report_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    report_dir = report_path + report_name + report_time + ".html"
    with open(report_dir, 'wb') as file_path:
        runner = HTMLTestRunner(stream=file_path, title="API自动化测试报告", description='API模块用例', verbosity=2)
        runner.run(testcases)
    # SendMail().send_email()


if __name__ == '__main__':
    run()