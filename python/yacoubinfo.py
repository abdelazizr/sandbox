import os
import time
import datetime
import logging

def log_port_activity():
# running the command scan port
    
    my_Ports = "netstat /a > C:\\temp\\mypythonfiles\\port.txt"
    os.system(my_Ports)
# creating time-stamp string folder and files name
def timeStamped(portsactivity_fmt='{fname}_%H_%M_%d_%m_%Y_.log'):
    fname = timeStamped(portsactivity.log)
    return datetime.datetime.now().strftime().format(fname)
    print(now)
portsactivity = "C:\\temp\\mypythonfiles\\port.txt"
cool_file = open(portsactivity, "r")

for xdoc in cool_file:
    if (xdoc.find("ESTABLISHED")>0) or (xdoc.find("LISTENING") > 0):
        print(xdoc)




#timeStamped()
cool_file.close 
log_port_activity()


