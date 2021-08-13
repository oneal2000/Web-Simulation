with open('urls_with_note', 'a') as myFile:
    i = 8.000
    while True:
        myFile.write(str(i)[0:5]+',\n')
        i +=0.72
        if(i>16):
            break
