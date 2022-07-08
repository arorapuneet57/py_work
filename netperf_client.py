# python3 netperf_client.py 2000:10:1::30 2000:1:1::21
import os
import sys
import signal
import threading
import time

server_ip = sys.argv[1]
client_ip = sys.argv[2]


def execute_command():
    cmd = "/automation/bin/x86_64/linux/netperf  -6   -p 49162   -l 2   -H %s -L %s   -t tcp_stream --   MAGIC165726040122324 > /tmp/client.txt" % (server_ip, client_ip)
    print(cmd)
    os.popen(cmd).read()
    output_file()

def output_file():
    print(os.popen("cat /tmp/client.txt").read())


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        print("killing netperf process!!!!")
        os.popen("ps -aef | grep netperf | awk {'print $2'} | head -n1 | xargs kill -9")
        print("netperf process killed !!!!")
        exit(1)

signal.signal(signal.SIGINT, handler)

if __name__ == "__main__":
    #t1 = threading.Thread(target=execute_command)
    #t2 = threading.Thread(target=output_file)
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()
    signal.signal(signal.SIGINT, handler)
    for i in range(1, 10000):
        execute_command()
        time.sleep(1)
