from selenium import webdriver
import time
from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
# 下载浏览器的驱动,详情可见参考https://www.jianshu.com/p/1b63c5f3c98e
driver = webdriver.Chrome(executable_path=r'')#这里填驱动的绝对路径,火狐就将Chrome改为Firefox
driver.get(r'http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn')#兰州大学个人工作台
driver.implicitly_wait(30)
username=driver.find_element_by_id('username')
password=driver.find_element_by_id('password')
username.send_keys('*') #填写校园卡号
password.send_keys('*') #兰大个人工作平台登录密码
button=driver.find_element_by_tag_name('button')
button.click()#登录

mouse=driver.find_element_by_xpath('//*[@id="my-apps"]/li[1]/a/div[2]/p[1]')
#注意在个人工作台将健康打卡加入我的应用，其中li后面的序号为健康打卡模块在我的应用中的顺序，我这里放在了最前面，所以是li[1]

ActionChains(driver).move_to_element(mouse).perform()#把鼠标放到健康打卡图标上，出现“进入”和“移除”
inp=driver.find_element_by_xpath('//*[@id="my-apps"]/li[1]/a/div[2]/p[2]/span[1]')
inp.click()#点击“进入”进入健康打卡模块

iframe=driver.find_element_by_tag_name('iframe')#找到弹窗

driver.switch_to_frame(iframe)

shanggbao=driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[12]/uni-button')
shanggbao.click()#点击上报

#基本信息上报
# jibenxinxi=driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]')
# jibenxinxi.click()
#
# queding2=driver.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
# queding2.click()
#
# shangbao2=driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-view/uni-button')
# shangbao2.click()
current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
logger.add("daka.log")
print("{}打卡成功！".format(current_time))
logger.info("{}打卡成功！".format(current_time))
driver.quit()
