import socket 
import platform 
from datetime import datetime  
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

currentdate = datetime.now()
#timestamp = datetime.timestamp(currentdate)

print("Date and time is:", currentdate)
print("Timestamp is:", timestamp)   
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr) 
print(platform.node())
print(platform.system())
