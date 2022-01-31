import json
import re
import os

myfile = open('data.json','r+')
data = json.loads(myfile.read())

class Validate:
     
    def __init__(self):
        pass
        
    def validate_ip(self,*ip_addr):
        self.ip_addr = ip_addr
        
        print("Recived Ip from json file:",ip_addr[0])
        regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        
        for i in range(len(ip_addr[0])):
            print("Validating IP",ip_addr[0][i])
            
            try:
                if(re.search(regex,ip_addr[0][i])):
                    if (re.search(r"10|172|192",ip_addr[0][i].split('.')[0])):
                        print("This is Reserved IP")
                            
                    print("ip is valid, proceeding for the ping")
                    os.system("ping -n 1 "+ip_addr[0][i])
                else:
                    raise Exception()
            except:
                print("ip is not valid")
            print(end="\n")
    
ipObj=Validate()
ipObj.validate_ip(data['ipaddr'])