import json
import re
import os

myfile = open('data.json','r+')
data = json.loads(myfile.read())

class Validate:
     
    def __init__(self,*ip_addr):
        self.ip_addr = ip_addr
        
        print("Recived Ip from json file:",ip_addr[0])
        regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        
        for i in range(len(ip_addr[0])):
            print("Validating IP",ip_addr[0][i])
            try:
                if(re.search(regex,ip_addr[0][i])):
                    print("ip is valid,Validating the ping")
                    os.system("ping -n 1 "+ip_addr[0][i])
                else:
                    raise Exception()
            except:
                print("ip is not valid")
    
Validate(data['ipaddr'])