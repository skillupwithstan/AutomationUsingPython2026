# Service Related
#import psutil
import getpass
pwd = getpass.getpass()

'''
def getService(name):
    serviceStatus = None
    try:
        serviceStatus = psutil.win_service_get(name)
        serviceStatus = serviceStatus.as_dict()
        return serviceStatus
    except Exception as ex:
        print(str(ex))

servicename = input("Enter the service name:")
if(servicename != ""):
    for i in servicename.split(","):
        service_result = getService(i.strip())
        #print(service_result)
        print("Service Name:",service_result["name"])
        print("Service Display Name:",service_result["display_name"])
        print("Service Status:",service_result["status"])
else:
    print("Please enter the valid Service Name")

print("***********************************************")

import psutil

print(psutil.cpu_count())
print(psutil.disk_usage("D:"))

import shutil

print(shutil.disk_usage("D:"))

total, used, free = shutil.disk_usage("D:")

print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)))

print("***********************************************")

import win32serviceutil
#print(win32serviceutil.QueryServiceStatus("spooler", "localhost")) 
# 1 - Stopped; 2 - StartPending; 3 - StopPending; 4 - Running;
#win32serviceutil.StopService("spooler")
#win32serviceutil.StartService("winrm")

import win32serviceutil
#def service_running(service, machine):
#    return win32serviceutil.QueryServiceStatus(service, machine)[1] == 4

def service_info(action, machine, service):
    #running = service_running(service, machine)
    servicename = 'service (%s) on machine (%s)' % (service, machine)
    action = action.lower()
    if action == 'stop':
        win32serviceutil.StopService(service, machine)
        print('%s stopped successfully' % servicename)
    elif action == 'start':
        win32serviceutil.StartService(service, machine)
        print('%s started successfully' % servicename)
    elif action == 'restart':
        win32serviceutil.RestartService(service, machine)
        print('%s restarted successfully' % servicename)
    elif action == 'status':
        if(win32serviceutil.QueryServiceStatus(service, machine)[1] == 4):
            print("%s is running" % servicename)
        else:
            print("%s is not running" % servicename)
    else:
        print("Unknown action (%s) requested on %s" % (action, servicename))

# Special variable used to store code that should only run when the file is executed as a script
if __name__ == '__main__':
    machine = 'localhost'
    service = 'winrm'
    action = 'status'
    service_info(action, machine, service)

import wmi

# For Connection
c = wmi.WMI()
#print(c.classes)
#print(c.Win32_Service())
#print(c.Win32_Service.methods.keys())
#print(c.Win32_Service.properties.keys())  

#for s in c.Win32_Service():
#    print(s.Name,"-",s.State)

import wmi
# For Connection
c = wmi.WMI()

# Iterate through all logical disks
for disk in c.Win32_LogicalDisk():
    # Print disk details
    print(f"Device ID: {disk.DeviceID}")
    print(f"File System: {disk.FileSystem}")
    print(f"Total Size: %d GB" % (int(disk.Size) / (2**30)))
    print(f"Free Space: %d GB" % (int(disk.FreeSpace) / (2**30)))
    print(f"Volume Name: {disk.VolumeName}")
    print("-" * 25)

print("***********************************************")

import getpass
pwd = getpass.getpass()

print("***********************************************")

import psutil, mysql.connector, getpass

dbdetails = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = getpass.getpass(),
  database = "PythonApp"
)

def getService(name):
    #service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
        return service
    except Exception as ex:
        print(str(ex))

while True:
    servicename = input("Enter the service name:")
    if(servicename != ""):
        for i in servicename.split(","):
            service_result = getService(i.strip())
            try:
                mycursor = dbdetails.cursor()
                query = "INSERT INTO SERVICE_DETAILS (name, description, status) VALUES ("+ "'" + service_result["name"] +"',"+ "'"+ service_result["display_name"]+ "',"+ "'"+ service_result["status"] +"')"
                print(query)
                mycursor.execute(query)
                dbdetails.commit()
                print(mycursor.rowcount, "record inserted.")
            except Exception as ex:
                print(ex)
    else:
        print("Please enter the valid Service Name")
        break
'''