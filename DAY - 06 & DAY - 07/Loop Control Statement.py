'''
#pass
num=10
count=0
while(count <= num):
    if(count%2 == 0):
        pass
        print("COUNT: ", count)
    else:
        print(count)
    count += 1

print("********************************************")

#break
for i in range(3):
    for j in range(3):          
        if j==2:    
            break
            print(j)
        print("The number is ",i,j)

print("********************************************")

#continue
for i in range(3):
    for j in range(2):          
        if i==1:    
            continue
        print("The number is ",i,j)

for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            pass
            print("Add User "+ user + " for " + server)

print("*******************************************")

for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            break
        print("Add User "+ user + " for " + server)

print("*******************************************")

for server in "server01","server02","server03":
    for user in "user01","user02","user03":
        if(user == "user02"):
            continue
        print("Add User "+ user + " for " + server)

print("*******************************************")

'''

services = input("Enter the services do you want to stop:")
for service in services.split(","):
    if(service != "winrm"):
        print("The service " + service + " is stopped successfully.")
    else:
        print("The service " + service + " should not be stopped") 
