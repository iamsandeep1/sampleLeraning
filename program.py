import json
import re
import os

class Validate:
     
    def __init__(self):
        pass
    
    def validate_ip(self,jsonFile):
        self.jsonFile = jsonFile
        with open(jsonFile) as file:
            data = json.load(file)
            
        for ip_addr in data['ipaddr']:
            print("Recived Ip from json file:",ip_addr)
            regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            print("Validating IP",ip_addr)
            try:
                if(re.search(regex,ip_addr)):
                    if (re.search(r"10|172|192",ip_addr.split('.')[0])):
                        print("This is Reserved IP")
                            
                    print("ip is valid, proceeding for the ping")
                    os.system("ping -n 1 "+ip_addr)
                else:
                    raise Exception()
            except:
                print("ip is not valid")
            print(end="\n")
    
ipObj=Validate()
ipObj.validate_ip('data.json')