import sys
query=(sys.argv[1])
api = "https://www.sogou.com/web?query="
# query = input("请输入查询关键词:")
url = api+query
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
js = '''
function insertStr(soure, start, newStr){
    return soure.slice(0, start) + newStr + soure.slice(start);
}
function myFc() {
    var str = '<div style="position: relative;left: 400px;top: 20px;"><iframe height="100" width="100" align="right" scrolling="no" src="https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A%255B%257B%2522f%2522%253A%252210%2522%252C%2522text%2522%253A%2522%2522%257D%255D%252C%2522boxOpts%2522%253A%257B%2522showInfo%2522%253Afalse%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B%2522cols%2522%253A1%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C%2522duration%2522%253Anull%257D%257D"></iframe></div>'
    var x = document.getElementsByClassName("vrwrap");
    for(var i=0;i<x.length;i++){
        x[i].innerHTML = insertStr(x[i].innerHTML,0,str);
    }
    var y = document.getElementsByClassName("right");
    for(var i=0;i<y.length;i++){
        y[i].innerHTML = '';
    }
}
myFc()
'''
driver.execute_script(js)