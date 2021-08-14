import socket
import sys
import time
from selenium import webdriver

# win + ctrl + D  切换桌面
from pykeyboard import PyKeyboard
k = PyKeyboard()
k.press_key(k.windows_r_key)
k.press_key(k.control_l_key)
k.tap_key('d')
k.release_key(k.windows_r_key)
k.release_key(k.control_l_key)




query=(sys.argv[1])
api = "https://www.sogou.com/web?query="
# query = input("请输入查询关键词:")
url = api+query
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

js_add_funtional_ssvep = '''
function insertStr(soure, start, newStr){
    return soure.slice(0, start) + newStr + soure.slice(start);
}
function add_funtional_ssvep(){
    var urls = ["https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25228%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25228.72%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25229.44%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210.16%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210.88%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252211.60%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252212.32%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252213.04%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252213.76%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252214.48%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", ];
    var x = document.getElementsByTagName("body");
    var str = '<div style="position: fixed;zIndex:9999;left: 40px;top: 40px;"><iframe height="100" width="100" align="right" scrolling="no" src="' + urls[9] + '"></iframe></div>'
    var str1 = '<div style="position: fixed;zIndex:9999;right: 40px;top: 40px;"><iframe height="100" width="100" align="right" scrolling="no" src="' + urls[7] + '"></iframe></div>'
    var str2 = '<div style="position: fixed;zIndex:9999;right: 40px;bottom: 40px;"><iframe height="100" width="100" align="right" scrolling="no" src="' + urls[8] + '"></iframe></div>'
    x[0].innerHTML = insertStr(x[0].innerHTML,0,str);
    x[0].innerHTML = insertStr(x[0].innerHTML,0,str1);
    x[0].innerHTML = insertStr(x[0].innerHTML,0,str2);
    
}
add_funtional_ssvep()
'''


js = '''
function insertStr(soure, start, newStr){
    return soure.slice(0, start) + newStr + soure.slice(start);
}
function myFc1() {
    var str = '<div style="position: relative;left: 400px;top: 20px;"><iframe height="100" width="100" align="right" scrolling="no" src="https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Afalse%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D"></iframe></div>'
    var urls = ["https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25228%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25228.72%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25229.44%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210.16%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210.88%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252211.60%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252212.32%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252213.04%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252213.76%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252214.48%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", ];
    var x = document.getElementsByClassName("vrwrap");
    for(var i=0;i<x.length;i++){
        x[i].innerHTML = insertStr(x[i].innerHTML,0,str);
    }
    var y = document.getElementsByClassName("right");
    for(var i=0;i<y.length;i++){
        y[i].innerHTML = '';
    }
}
function myFc() {
    // var str = '<div style="position: relative;left: 400px;top: 20px;"><iframe height="100" width="100" align="right" scrolling="no" src="https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Afalse%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D"></iframe></div>'
    var urls = ["https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25228%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25228.72%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%25229.44%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210.16%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210.88%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252211.60%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252212.32%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252213.04%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252213.76%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", "https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252214.48%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D", ];
    var x = document.getElementsByClassName("vrwrap");
    for(var i=0;i<x.length;i++){
        var str = '<div style="position: relative;left: 400px;top: 20px;"><iframe height="100" width="100" align="right" scrolling="no" src="' + urls[i] + '"></iframe></div>'
        x[i].innerHTML = insertStr(x[i].innerHTML,0,str);
        if(i>6){
            break;
        }
    }
    var y = document.getElementsByClassName("right");
    for(var i=0;i<y.length;i++){
        y[i].innerHTML = '';
    }
    var y = document.getElementsByClassName("header");
    y[0].innerHTML = '';
    
}
myFc()
'''
driver.execute_script(js)
driver.execute_script('window.scrollBy(0,40)')

# links to SSVEP Stimulations
SSs = []
driver.execute_script(js_add_funtional_ssvep)

# 设置TCPIP连接
MaxBytes = 1024 * 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(60*120)
host = '127.0.0.1'
port = 11223
server.bind((host, port))
server.listen(1)

# 除了打开网页以外，还需要在网页上添加SSVEP刺激
def open_website(id):
    elements = driver.find_elements_by_class_name("vrwrap")
    judge = elements[id].find_elements_by_class_name('vr-title')
    if len(judge) != 0:
        tmp = elements[id].find_element_by_class_name('vr-title')  # .click()
        tmp.find_element_by_tag_name("a").click()
    else:
        try:
            tmp = elements[id].find_element_by_class_name('vrTitle')  # .click()
            tmp.find_element_by_tag_name("a").click()
        except:
            print("bad click")
    handle = driver.current_window_handle
    handles = driver.window_handles
    # 对窗口进行遍历
    for newhandle in handles:
        if newhandle != handle:
            driver.switch_to.window(newhandle)
    time.sleep(3)
    driver.execute_script(js_add_funtional_ssvep)

    # try:
    #     elements[id].find_element_by_class_name('vr-title').click()
    # except:
    #     elements[id].find_element_by_class_name('vrTitle').click()



def scroll_up():
    driver.execute_script('window.scrollBy(0,-800)')


def scroll_down():
    driver.execute_script('window.scrollBy(0,800)')


def close_page():
    handle = driver.current_window_handle
    handles = driver.window_handles
    if len(handles)==1:
        driver.close()
        k.press_key(k.windows_r_key)
        k.press_key(k.control_l_key)
        k.tap_key(k.left_key)
        k.tap_key(k.left_key)
        k.tap_key(k.left_key)
        k.release_key(k.windows_r_key)
        k.release_key(k.control_l_key)
        exit(0)
        return
    for newhandle in handles:
        if newhandle != handle:
            driver.close()
            driver.switch_to.window(newhandle)
            return


def process(id):
    # 映射1
    # id = (id-8)/0.72

    # 映射2
    # id = int((id+0.25-8)/0.72)
    if(id==0):
        open_website(id)
    if(id==1):
        open_website(id)

    if(id==2):
        open_website(id)

    if(id==3):
        open_website(id)

    if(id==4):
        open_website(id)

    if(id==5):
        open_website(id)

    if(id==6):
        open_website(id)

    if(id==7):
        scroll_up()

    if(id==8):
        scroll_down()

    if(id==9):
        close_page()

    if(id == 10086):
        exit(-1)

def listen():
    while True:
        client, addr = server.accept()
        while True:
            data = client.recv(MaxBytes)
            if not data:
                break
            rev_msg = (data.decode())
            print('recieve from matlab: ',rev_msg)
            process(int(rev_msg))
            return


while True:
    listen()