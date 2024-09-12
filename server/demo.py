import subprocess
import threading
import zlib
from PIL import Image

def find_IP():
    string= subprocess.check_output(["ipconfig"]).decode()
    string= string.replace("\r","")
    lines= string.split("\n")
    ips= []
    zerotier_networks= []
    in_zerotier= False
    for l in lines:
        if l!="" and l[0]!=" " and len(zerotier_networks)>len(ips):
            print(l.encode())
            zerotier_networks.pop(-1)
            in_zerotier=False
        if l[:25]=="Ethernet adapter ZeroTier":
            zerotier_networks.append(l)
            in_zerotier=True
        if in_zerotier and l[:15]=="   IPv4 Address":
            ips.append(l)
            in_zerotier=False

    print(zerotier_networks)
    print(ips)
    
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
        print(splited)
        for n in splited:
            num+=int(n)*digit
            digit*=256
    print(num)
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

im = Image.open("window no network.png")
ans= im.resize((800,800))
ans.save("window no network resized.png")
