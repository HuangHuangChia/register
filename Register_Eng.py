#網掛英文版
import requests
import codecs
import pathlib

change=[180,204,218,220]
#change=[180,214,228,230]
#change=[228,230]
currentpath=str(pathlib.Path().absolute())+"\\"

url='https://register.typc.mohw.gov.tw/OINetReg/OINetReg.Reg/Reg_NetReg.aspx?lang=E'

path=currentpath+"Register_Eng_Html_old.txt"
#print(path)
path1=currentpath+"Register_Eng_Html_new.txt"

#path_counter=currentpath+"Register_Eng_counter.txt"
path_error=currentpath+"Register_Eng_error.txt"
path_info=currentpath+"Register_Eng_info.txt"

res=requests.get(url)
res.encoding = 'utf-8'


f = open(path1, mode="w",encoding="utf-8")
f.write(res.text)
f.close()

f= open(path, mode='r',encoding='UTF-8')
content_old=f.readlines()
f.close()

f1= open(path1, mode='r',encoding='UTF-8')
content_new=f1.readlines()
f1.close()

f2 = open(path_error, mode="w",encoding="utf-8")

f2.write("網掛EnglishVersion"+"\n")

i=0
different=0
if len(content_new) != len(content_old):
    f2.write("新舊網頁長度不同,原行數+"+str(len(content_old))+" 新行數"+str(len(content_new))+"\n")
while i<len(content_new) and  i<len(content_old) :
    if (content_old[i] != content_new[i]) and not(i in change):
        print("line",i)
        print(content_old[i],content_new[i])
        f2.write("line "+str(i)+"\n")
        f2.write(content_old[i]+content_new[i])
        different+=1
    i+=1
f2.close()


f3 = open(path_info, mode="w",encoding="utf-8")
f3.write("網掛EnglishVersion")
if different==0 and len(content_new) == len(content_old):
    f3.write("測試無異常")
else:
    if len(content_new) != len(content_old):
        f3.write("新舊網頁長度不同,原行數"+str(len(content_old))+" 新行數"+str(len(content_new))+".")
    if different>0:
        f3.write("與前版比較有"+str(different)+"項不同.")
    f3.write("請確認")
f3.close() 

print('done')

