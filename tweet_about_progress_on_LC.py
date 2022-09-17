import re

def file_read(filename):
    fhand = open(filename,'r')
    txt = ''
    txt2 = list()
    cnt = 0 
    for lines in fhand:
        lines  = lines.strip()
        if bool(re.search('^LC := ([0-9]+).',lines)):
            txt = txt + "LC:= " + re.findall('[0-9]+.',lines)[0] +' '
            cnt+=1
            if(cnt > 10):
                txt = txt + '\n'
                cnt = 0
            txt2.append(lines)

    print("Number of problems solved so far (starting from 21st August 2022) := ",len(txt2))
    print(txt)
    print(len(txt))
    fhand.close()


file_name = input('Enter Filename := ')
file_read(file_name)
