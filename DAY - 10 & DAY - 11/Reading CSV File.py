'''
fcsv = open("sample.csv")
print(fcsv.readlines())
print(fcsv.read())
'''

file1 = open("sample.csv")
data1 = file1.read()
file1.close()

file2 = open("test.csv")
data2 = file2.read()
file2.close()

type(data1)

for server in data1.splitlines():
    for sid in data2.splitlines():
        if((server.split(",")[0] == "server2") and (sid.split(",")[0] == "server2")):
            result = server.split(",")[0] + "," + server.split(",")[1] + "," + sid.split(",")[1]
            print(result)
