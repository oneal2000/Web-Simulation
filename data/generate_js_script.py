urls = []
# 提取出之前存在文件中的url
i = 0
with open('urls_with_note','r') as myFile:
    while True:
        line = myFile.readline()
        str = (line.split(',')[1].strip('\n'))
        if not line:
            break
        # print(line.strip(',')[1].strip('\n'))
        urls.append(str)
        print(str)
        i += 1
        if(i==10):
            break



# var fruits = ["Banana", "Orange", "Apple", "Mango"];
with open('var.js','a') as myFile:
    myFile.write('var urls = [')
    for i in range(0,len(urls)):
        myFile.write('\"')
        myFile.write(urls[i])
        myFile.write('\", ')
    myFile.write('];')