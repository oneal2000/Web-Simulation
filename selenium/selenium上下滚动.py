api = "https://www.sogou.com/web?query="
query = input("请输入查询关键词:")
url = api+query
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url)
driver.execute_script('window.scrollBy(0,800)')
