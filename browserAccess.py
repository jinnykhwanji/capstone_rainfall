import webbrowser
from time import localtime, strftime

#Get the time data
print(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))
date,month,year,hour=strftime("%d",localtime()),strftime("%m",localtime()),strftime("%Y",localtime()),strftime("%H",localtime())
print(date)
print(month)
print(year)
print(hour)
time_slot=["00","06","12","18"]
i= int(int(hour)/6)
time_interval=time_slot[i]

#call the website
url = "https://ftp.wpc.ncep.noaa.gov/shapefiles/qpf/day1/94q_"+year+month+date+time_interval+".tar"
webbrowser.get('chrome').open(url)

#open up the zip folder& extract data

#open up ArcGIS and import the shapefile in the folder



