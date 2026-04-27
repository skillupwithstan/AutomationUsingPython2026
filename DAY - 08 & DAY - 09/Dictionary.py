# Dictionary with keys and values of different data types
numbers = {"key1": "One", "key2": "Two", "key3": "Three"}
print(numbers)
print(numbers["key2"])

numbers["key4"] = "Four"
print(numbers)

numbers["key3"] = "No-3"
print(numbers)

del numbers["key3"]
print(numbers)

#Loop
for key,value in numbers.items():
    print(key,"=",value)

#To extract dictionary keys 
print(numbers.keys())

#To extract dictionary values
print(numbers.values())

#To extract both dictionary key and values
print(numbers.items())  #print(numbers)
'''

numbers1 = numbers
print(numbers1)

message="Welcome to Chennai"
word=message[-7:]
if(word=="Chennai"):
    print("got it")
else:
    message=message[3:14]
    print(message)

'''
