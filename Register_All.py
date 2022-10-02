#網掛中文版
import requests
import codecs
import pathlib
import sendmail
import os
#web=[0:2]  #檢查三個網頁
change=[[],[180,190,214,228,230],[180,204,218,220]]

currentpath=str(pathlib.Path().absolute())+"\\"


url=['https://register.typc.mohw.gov.tw/OINetReg',
     'https://register.typc.mohw.gov.tw/OINetReg/OINetReg.Reg/Reg_NetReg.aspx',
     'https://register.typc.mohw.gov.tw/OINetReg/OINetReg.Reg/Reg_NetReg.aspx?lang=E']

path=[currentpath+"Register_Main_Html_old.txt",currentpath+"Register_Chn_Html_old.txt",currentpath+"Register_Eng_Html_old.txt"]
path1=[currentpath+"Register_Main_Html_new.txt",currentpath+"Register_Chn_Html_new.txt",currentpath+"Register_Eng_Html_new.txt"]

#path_counter=currentpath+"Register_Chn_counter.txt"
path_error=[currentpath+"Register_Main_error.txt",currentpath+"Register_Chn_error.txt",currentpath+"Register_Eng_error.txt"]
#path_info=[currentpath+"Register_Chn_info.txt"
path_info=currentpath+"Register_All_info.txt"
title=['網掛主網頁','網掛中文版','網掛EnglishVersion']
#f3 = open(path_info, mode="w",encoding="utf-8")
notify=""
status=0
for web in range(3):           
    res=requests.get(url[web])
    res.encoding = 'utf-8'


    f = open(path1[web], mode="w",encoding="utf-8")
    f.write(res.text)
    f.close()

    f= open(path[web], mode='r',encoding='UTF-8')
    content_old=f.readlines()
    f.close()

    f1= open(path1[web], mode='r',encoding='UTF-8')
    content_new=f1.readlines()
    f1.close()

    f2 = open(path_error[web], mode="w",encoding="utf-8")

    f2.write(title[web]+"\n")

    i=0
    different=0
    if len(content_new) != len(content_old):
        f2.write("新舊網頁長度不同,原行數+"+str(len(content_old))+" 新行數"+str(len(content_new))+"\n")
    while i<len(content_new) and  i<len(content_old) :
        if (content_old[i] != content_new[i]) and not(i in change[web]):
            print("line",i)
            print(content_old[i],content_new[i])
            f2.write("line "+str(i)+"\n")
            f2.write(content_old[i]+content_new[i])
            different+=1
        i+=1
    f2.close()


    notify+=title[web]
    #f3.write(title[web])
    if different==0 and len(content_new) == len(content_old):
        #f3.write("測試無異常.")
        notify+="測試無異常."
    else:
        status+=1
        if len(content_new) != len(content_old):
            #f3.write("新舊網頁長度不同,原行數"+str(len(content_old))+" 新行數"+str(len(content_new))+".")
            notify+="新舊網頁長度不同,原行數"+str(len(content_old))+" 新行數"+str(len(content_new))+"."
        if different>0:
            notify+="與前版比較有"+str(different)+"項不同."
            #f3.write("與前版比較有"+str(different)+"項不同.")
        #f3.write("請確認")
        notify+=",請確認"

if status==0:
    if(os.path.isfile(path_info)): #刪除狀態檔及比較內容檔
        os.remove(path_info)
else:
    with open(path_info, mode="w",encoding="utf-8") as f3:
        f3.write(notify)
        sendmail._sendmail_inlist(send_user = 'WebPage Test<Doraemon@typc.mohw.gov.tw>' ,receive_users = '<info@typc.mohw.gov.tw>',
              subject = notify,email_text = notify,
              server_address = 'msa.hinet.net',file = path_error )       
#sendmail._sendmail_inlist(send_user = 'WebPage Test All<Doraemon@typc.mohw.gov.tw>' ,receive_users = '<honga@typc.mohw.gov.tw>',
#              subject = notify,email_text = notify,
#              server_address = 'msa.hinet.net',file = path_error )  

#f3.close() 

print('done')

