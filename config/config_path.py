# -*- coding: utf-8 -*-
import os
# 项目文件的绝对路径
base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


# driver路径
chrome_path = os.path.join(base_path, 'drivers', 'chromedriver.exe')
ie_path = os.path.join(base_path, 'drivers', 'IEDriverServer.exe')
firefox_path = os.path.join(base_path, 'drivers', 'geckodriver.exe')

# yaml文件路径
read_yaml_path = os.path.join(base_path, 'config', 'data.yaml')
write_yaml_path = os.path.join(base_path, 'config', 'extract.yaml')

# excel文件路径
excel_path = os.path.join(base_path, 'data', 'interface.xlsx')

# 截图路径
picture_path = os.path.join(base_path, 'result/SCRshot/')

# 日志路径
log_path = os.path.join(base_path, "result/logs/")

# 报告路径
report_path = os.path.join(base_path, 'result/report/')




