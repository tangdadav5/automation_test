# import uiautomator2  as ui2
# import time
#
#     driver=ui2.connect('emulator-5554')
#     #driver=ui2.connect_usb('') #连接真机
#     # app_name=driver.app_current()
#     # print(app_name) #com.netease.cloudmusic  查看当前运行的app包名
#     # device_info=driver.device_info #获取当前设备信息
#     # print(device_info['display'])  #设备的 宽，高
#     driver.app_start('com.netease.cloudmusic')#启动app
#     driver(resourceId="com.netease.cloudmusic:id/rl", text="最近播放").click()
#     driver.click(0.825, 0.469)