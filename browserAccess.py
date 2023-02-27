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
url="https://api.openweathermap.org/data/2.5/forecast?lat=38.03&lon=-78.51&appid=5bb9d4eaa5770bd3017fe3dbe64e438a"


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

    
        
    
"""
#http://api.openweathermap.org/maps/2.0/radar/forecast/7/36/49?&appid={4221c1c9a173822cefd267a5591a3bf3}&tm=1677463393
#webbrowser.get('chrome').open(url)

#url = "http://api.openweathermap.org/maps/2.0/radar/forecast/7/"+str(x)+"/"+str(y)+"?&appid={5bb9d4eaa5770bd3017fe3dbe64e438a}&tm=1677463393"
#url="https://api.agromonitoring.com/agro/1.0/weather/forecast?lat=38=-79&appid={4221c1c9a173822cefd267a5591a3bf3}"
#url="https://api.openweathermap.org/data/3.0/onecall?lat=38&lon=-79&exclude=current,minutely&appid=5bb9d4eaa5770bd3017fe3dbe64e438a"

#all_pre=all_data[8]

#print(all_pre)
#print(all_pre.get('rain'))
#print(all_pre.get('dt_txt'))
#print(response.json().get('list').get('rain.3h'))


#page = urlopen(url)
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")
#print(html)

#https://maps.openweathermap.org/maps/2.0/radar/forecast/3/38.033554/-78.507980?&appid={5bb9d4eaa5770bd3017fe3dbe64e438a}&tm=1677463393


#name="94q_"+year+month+date+time_interval+".tar"
#https://api.weather.gov/gridpoints/LWX/50,26
#https://api.weather.gov/points/38.033554,-78.507980
#url = "https://api.weather.gov/gridpoints/LWX/50,26"
#webbrowser.get('chrome').open(url)
#req=urllib.request.Request(url)
#with urllib.request.urlopen(req) as resp:
#    ds = xr.open_dataset(io.BytesIO(resp.read()))
#resp=urllib.request.urlopen(req)
#data=resp.read()
"""


'''
name="94q_"+year+month+date+time_interval+".tar"
url = "https://ftp.wpc.ncep.noaa.gov/shapefiles/qpf/day1/"+name
webbrowser.get('chrome').open(url)'''



'''
#open up the zip folder& extract data
import tarfile

file=tarfile.open('/Users/jinny/Downloads/'+name)
print(file.getnames())
file.extractall('/Users/jinny/Desktop/Capstone')
file.close() #be able to get the shape file now (name 94q3012.shp) (94q+last4 digits)


#open up ArcGIS and import the shapefile in the folder
import arcpy
import numpy
arcpy.env.workspace=r"/Users/jinny/Desktop/Capstone/94q3012.shp"
'''

