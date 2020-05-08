import time
from datetime import datetime as dt
host_path = r"c:\Windows\System32\Drivers\etc\hosts"
#host_path = r"D:\projects\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]
while(True):
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        #WORKING HOURS
        print("WORKING HOURS")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("FUN HOURS")
        #FUN HOURS
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)