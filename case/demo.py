from appium import webdriver
import time

# apk参数
desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.tencent.mm',  # apk的包名
                        'appActivity': 'com.tencent.mm.ui.LauncherUI'  # activity 名称
                        }
# 启动app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
driver.implicitly_wait(10)
# 我的app启动后是欢迎页，需要滑动
# 获取屏幕尺寸
sizes = driver.get_window_size()
# 滑动
# driver.swipe(sizes.get('width')*0.9, sizes.get('height')*0.5, sizes.get('width')*0.2, sizes.get('height')*0.5)
# 加入已经跳转到h5中
# 打印所有的context
contexts = driver.contexts
print(contexts)
# ['NATIVE_APP', 'WEBVIEW_com.sdguodun.qyoa']
# NATIVE_APP 就是安卓原生的
# WEBVIEW_com.sdguodun.qyoa 就是h5的
# 切换到h5
# driver.switch_to.context('WEBVIEW_com.sdguodun.qyoa')
# 定位到元素，输入test
# driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/input').send_keys('test')
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
time.sleep(3)
driver.quit()