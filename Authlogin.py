from selenium import webdriver
import time
from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
# 下载谷歌浏览器的驱动
driver = webdriver.Chrome(executable_path=r'E:\driver\chromedriver_win32\chromedriver.exe')
driver.get(r'http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn')
driver.implicitly_wait(30)
username=driver.find_element_by_id('username')
password=driver.find_element_by_id('password')
username.send_keys('*') #填写校园卡号
password.send_keys('*') #兰大个人工作平台登录密码
button=driver.find_element_by_tag_name('button')
button.click()

mouse=driver.find_element_by_xpath('//*[@id="my-apps"]/li[7]/a/div[2]/p[1]')

ActionChains(driver).move_to_element(mouse).perform()
inp=driver.find_element_by_xpath('//*[@id="my-apps"]/li[7]/a/div[2]/p[2]/span[1]')
inp.click()

iframe=driver.find_element_by_tag_name('iframe')

driver.switch_to_frame(iframe)

shanggbao=driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[12]/uni-button')
shanggbao.click()

queding=driver.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
queding.click()

jibenxinxi=driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]')
jibenxinxi.click()

queding2=driver.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
queding2.click()

shangbao2=driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-view/uni-button')
shangbao2.click()
current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
logger.add("daka.log")
print("{}打卡成功！".format(current_time))
logger.info("{}打卡成功！".format(current_time))
driver.quit()
