import sys
# query=(sys.argv[1])
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

api = "https://www.sogou.com/web?query="
# query = input("请输入查询关键词:")
query = 'swh'
url = api+query
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url)
elements  = driver.find_elements_by_class_name("vrwrap")

# for ele in elements:
# for i in range(0,len(elements)):
#     print(i,elements[i].text)

a = 1
elements[a].find_element_by_class_name('vr-title').click()
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").perform()

handle = driver.current_window_handle
handles = driver.window_handles
# 对窗口进行遍历
for newhandle in handles:
    if newhandle!=handle:
        driver.switch_to.window(newhandle)
        driver.close()