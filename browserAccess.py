from time import localtime, strftime
from urllib.request import urlopen

#Get the time data
print(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))
date,month,year,hour,min,sec=strftime("%d",localtime()),strftime("%m",localtime()),strftime("%Y",localtime()),strftime("%H",localtime()),strftime("%M",localtime()),strftime("%S",localtime())
print(date)
print(month)
print(year)
print(hour)
time_slot=["00","06","12","18"]
i= int(int(hour)/6)
time_interval=time_slot[i]

import datetime
import time
date_time = datetime.datetime(int(year), int(month), int(date), int(hour), int(min), int(sec))
 
# print regular python date&time
print("date_time =>",date_time)
 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))


#call the website
import webbrowser
url="https://api.openweathermap.org/data/2.5/forecast?lat=38.03&lon=-78.51&appid=+"+config.api_key


import requests
response = requests.get(url)
#print(response.status_code)
#print(response.json().keys()) 
all_data=response.json().get('list')
#print(len(all_data))
for i in range (0, len(all_data)):
    all_parameters=all_data[i]
    rain= all_parameters.get('rain')
    txt_time=all_parameters.get('dt_txt')
    print(str(rain)+"   "+str(txt_time))

    
        
