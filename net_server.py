#python3 net_server.py 2000:10:1::30
import os
import sys
import time
import signal

server_ip = sys.argv[1]

def execute_command():
    os.popen("/automation/bin/x86_64/linux/netserver -p 49162 -6 -L %s MAGIC165726034925362>> /tmp/server.txt" % server_ip).read()
    start_counter()

def start_counter():
    count = 0
    while(True):
        count = 1
        if count < 10000:
            time.sleep(1)
            print("traffic going on")
            count += 1
        else:
            break

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        print(os.popen("ps -aef | grep netserver | head -n1").read())
        print("killing netserver process!!!!")
        os.popen(" ps -aef | grep netserver | awk {'print $2'} | head -n1 | xargs kill -9")
        print("netserver process killed !!!!")
        print(os.popen("ps -aef | grep netserver | head -n1").read())
        exit(1)

signal.signal(signal.SIGINT, handler)

execute_command()
