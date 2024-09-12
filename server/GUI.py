from tkinter import *
from PIL import Image, ImageTk
import subprocess
import threading
import global_server_op

def find_IP():
    string= subprocess.check_output(["ipconfig"]).decode()
    string= string.replace("\r","")
    lines= string.split("\n")
    ips= []
    zerotier_networks= []
    in_zerotier= False
    for l in lines:
        if l!="" and l[0]!=" " and len(zerotier_networks)>len(ips):
            zerotier_networks.pop(-1)
            in_zerotier=False
        if l[:25]=="Ethernet adapter ZeroTier":
            zerotier_networks.append(l)
            in_zerotier=True
        if in_zerotier and l[:15]=="   IPv4 Address":
            ips.append(l)
            in_zerotier=False

    
    if len(zerotier_networks)>len(ips):
        zerotier_networks.pop(-1)
    
    if len(ips)!=len(zerotier_networks):
        print("find ip error")

    ans=[]
    
    for i in range(len(ips)):
        ips[i]= ips[i][39:]
        ans.append(zerotier_networks[i]+" "+ips[i])
        
    return (zerotier_networks,ips)
    #Ethernet adapter ZeroTier

def ips_zip(ips):
    num= 0
    letters="0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    digit=1
    for ip in ips:
        splited= ip.split(".")
        for n in splited:
            num+=int(n)*digit
            digit*=256
    ans=""
    while(num>0):
        ans+=letters[num%len(letters)]
        num= num//len(letters)
    return ans

def ips_unzip(string):
    letters="0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    num= 0
    digit=1
    for l in string:
        num+= letters.find(l)*digit
        digit*=len(letters)
    print(num)
    ans=[]
    while(num>0):
        ans.append([])
        for i in range(4):
            ans[-1].append(str(num%256))
            num= num//256

    for i in range(len(ans)):
        ans[i]= ".".join(ans[i])
    return ans

def main():
    global done
    root = Tk()
    root.geometry("800x800")
    root.title("server")

    text= ips_zip(find_IP()[1])
    if text=="":
        bg = PhotoImage(file="window no network resized.png")
    else:
        bg = PhotoImage(file="resized window.png") 
      
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0)

    if text!="":
        width= 40
        w = Text(root, height=len(text)//width+1, width=40, borderwidth=0)
        w.insert(1.0, text)
        w.configure(font = ("Arial",20),state="disabled") 
        w.place(x = 100, y = 325)
    root.mainloop()
    global_server_op.done= True
    
    
