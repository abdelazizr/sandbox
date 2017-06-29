# We are creating a function called check_services
import os
import time
import datetime

#first script
def check_service():
#hour = datetime.datetime.now()
#print(hour.hour)
#new_line = hour.hour
#print(type(new_line))
    new_line =datetime.datetime.now()
    hour= new_line.hour
    if (hour == 2):
        print("Security Services are about to be cycled")
        os.system("Lesson11_4.py")
print()
new_line =datetime.datetime.now()
hour= new_line.hour
if (hour != 2):
    if os.path.isdir("C:\\temp\\mypythonfiles"):
        pass
	
    else:
        os.makedirs("C:\\temp\\mypythonfiles")
    Done = "C:\\temp\\mypythonfiles\\currentServ.txt"
    my_Path = "net start > C:\\temp\\mypythonfiles\\currentServ.txt"
    os.system(my_Path)
    OPenfile=open (Done, "r")

    #found = FALSE
    FALSE = '0'
    for X in Done:
        found = FALSE
        #FALSE = '0'
        if(X.find("windows firewall") > 0):
            found = true
            print("Your Windows Firewall Service is ON")
            break
        else:
            print("The service Windows firewall was off, Now turning on Service!")
            break

            run = "net start advfirewall firewall"
            os.system(run)
            print("Now your Windows Firewall is on")
            
check_service()

input("enter to exit")


