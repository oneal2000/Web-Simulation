import sys
# query=(sys.argv[1])
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

api = "https://www.sogou.com/web?query="
# query = input("请输入查询关键词:")
query = 'cxs'
url = api+query
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url)
elements  = driver.find_elements_by_class_name("vrwrap")

id = 6
# elements[a].find_element_by_class_name('vr-title').click()
# print(elements[a].text)
# ele = elements[a].find_element_by_xpath('.//div[1]')
# ele.click()
# print(ele.text)
judge = elements[id].find_elements_by_class_name('vr-title')
if len(judge)!=0:
    tmp = elements[id].find_element_by_class_name('vr-title')#.click()
    tmp.find_element_by_tag_name("a").click()
else:
    try:
        tmp = elements[id].find_element_by_class_name('vrTitle')#.click()
        tmp.find_element_by_tag_name("a").click()
    except:
        print("bad click")


time.sleep(2)

