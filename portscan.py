#!/usr/bin/env python3.5
#coding: utf-8

from os import system
from sys import exit
from time import sleep
from socket import *

'''
PortScan
'''

def menu():
    system("reset")
    print("""
\033[41m========= Port Scan =========\033[1;m

""")
    

def options():
    menu()
    try:
        print("\033[31mChoice:\033[1;m \n")
        choice = int(input("  \033[1;91m[\033[1;m\033[1;32m1\033[1;m\033[1;91m]\033[1;m Scan Ports\n  \033[1;91m[\033[2;m\033[1;32m2\033[1;m\033[1;91m]\033[1;m Quit\n\n \033[1;91m\033[1;m "))
    except:
        print("\n\033[31mInvalid Choice\033[1;m")
        sleep(2)
        options()
        
    if choice == 1:
        scan()
    elif choice == 2:
        system("reset")
        exit(1)
    else:
         print("\n\033[31mInvalid Choice\033[1;m")
         sleep(2)
         options()

def scan():
    menu()
    try:
        host = input("\033[31mEnter the host:\033[1;m ")
        print("")
    except:
        scan()
    try:       
        ip = gethostbyname(host)
        print("\033[31mIP Address \033[1;m %s \n" %(ip))
    except:
        print("\033[31mHost invalid.\033[1;m")   
        sleep(3)
        scan()
    try:
        pi = int(input("\n\033[31mHome Port (ex: 80):\033[1;m "))
        print("")
    except:
        print("\033[31mInvalid Start Port.\033[1;m")
        sleep(3)
        scan()    
    try:
        pf = int(input("\033[31mEnd Port (ex: 443):\033[1;m "))
        print("\n")
    except:
        print("\033[31mEnd Door Invalid.\033[1;m")
        sleep(3)
        scan()         
        
    print("\033[33mStarting the Scan\033[1;m\033[32m...\033[1;m\n")  
    for i in range(pi, pf+1):
            sckt = socket(AF_INET, SOCK_STREAM)
            res = sckt.connect_ex((ip,  i))
            if (res == 0):
                print("\033[32mPort\033[1;m %d \033[32mOpen\033[1;m" %(i))
            else:
                print("\033[31mPort\033[1;m %d \033[31mClosed\033[1;m" %(i))
    print("\n\033[33mScan Completed\033[1;m\n")
    continu = input("\n\033[31mDo you want to do another Scan? (y/n):\033[1;m ")
    if continu == "y":
        scan()
    elif continu == "n":
        exit(1)
#sckt.close()

options() 
