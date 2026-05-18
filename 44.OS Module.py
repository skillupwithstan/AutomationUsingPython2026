import os
'''
os.system("ipconfig")
os.system("python --version")
os.system("systeminfo")

# Function to Get the current working directory
def current_path():
	print(os.getcwd())
	print()

print("Current working directory before:")		
current_path()
	
# Changing the CWD
os.chdir('..')
#os.chdir("C:")

print("Current working directory after:")			
current_path()

print("************************************")

# Directory
directory = "Logs"

# Parent Directory path
parent_dir = "C:/Users/X80119107/OneDrive - CCEP/Documents/SkillUp/Python/"

# Path
dirpath = os.path.join(parent_dir, directory)

os.mkdir(dirpath)
print("Directory '% s' created" % directory)

os.rmdir(dirpath)
print("Directory '" + directory +"' removed")

print("***************************************")

directory = "Logs"
parent_dir = "D:/Python/"
dirpath = os.path.join(parent_dir, directory)

os.makedirs(dirpath)
print("Directory '% s' created" % directory)
	
directory = "Input"
parent_dir = "D:/Python/Logs/"
dirpath = os.path.join(parent_dir, directory)

os.makedirs(dirpath)
print("Directory '% s' created" % directory)

#os.removedirs("Input")
'''
print("*********************************")

import os.path as p

print(p.abspath("LogFile.txt"))

print("*********************************")

#print(os.listdir("C:/Users/X80119107/OneDrive - CCEP/Documents/SkillUp/Python"))
#print(os.path.exists("C:/Users/X80119107/OneDrive - CCEP/Documents/SkillUp/Python"))
#print(os.path.getsize("C:/Users/X80119107/OneDrive - CCEP/Documents/SkillUp/Python"))

#import pathlib

# current working directory
#print(os.path.dirname(__file__))
