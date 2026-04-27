# Using with block option
with open("FileContent.txt") as server:
    data = server.read()
    #print(server.closed)
    server.close()
    #print(server.closed)
print(data)
	
'''
server = open("FileContent.txt")
content = server.read()
print(content)
server.close()
'''