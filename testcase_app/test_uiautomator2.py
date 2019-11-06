'''
uiautomator2环境安装，定位元素，实例
安装：pip install --pre uiautomator2
      pip install --pre -U weditor
      python -m uiautomator2 init ：初始化设备
      python -m weditor   打开本地浏览器：定位元素
定位元素：
resource-id:
     driver(resourceId="com.netease.cloudmusic:id/search_src_text")
text :
     driver(text="本地音乐")
description:
     driver(description='')
className
     driver(className='')
组合定位：
    driver(resourceId="com.netease.cloudmusic:id/search_src_text",className='')   
xpath:
     //*[@text="本地音乐"]
x，y坐标
    driver.click(0.321, 0.093) 比例
'''

import uiautomator2  as ui2
import time

driver=ui2.connect('10.200.11.112')
# driver=ui2.connect_usb('02194106C0800255') #连接真机
# app_name=driver.app_current()
# print(app_name) #com.netease.cloudmusic  查看当前运行的app包名
device_info=driver.device_info #获取当前设备信息
print(device_info['display'])  #设备的 宽，高
print(device_info)  #设备的 宽，高
# driver.app_start('com.netease.cloudmusic')#启动app
# driver(resourceId="com.netease.cloudmusic:id/rl", text="最近播放").click()
# driver.click(0.825, 0.469)

driver.app_start("com.yomobigroup.chat")
driver(text="Explore").click(timeout=10)
driver(text="Home").click(timeout=10)
driver(text="Following").click(timeout=10)
# driver(resourceId="com.yomobigroup.chat:id/ib_record").click()
driver(resourceId="com.yomobigroup.chat:id/user_header")[0].click(timeout=10)
