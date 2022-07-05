import requests   
from datetime import datetime                #Importing libraries
import re 
    

lat=input("Enter latitude value: ")          #Input the coordinates of the location
long=input("Enter longitude value: ")
date=input("Enter date in YYYY-MM-DD) format: ")
user_api=input("Enter your API KEY: ")       

complete_link="https://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+long+"&units=metric&appid="+user_api

link=requests.get(complete_link)
data=link.json() 

if data['cod']=='404':
    print("Invaild coordinates, please check the coordinates {},{}".format(lat,long))
    
else:
    print("\nCity: "+(data['city']['name']) +", Country Code: "+(data['city']['country']))
    print("\n----------------------------------------------------------------------------------------------------------\n")

    l=len(data['list'])

    for i in range(l):
        dt=data['list'][i]['dt_txt']
        dated = re.compile(r'\d{4}-\d{2}-\d{2}')
        d=re.match(dated,dt).group(0) 
        if d==date:
            date_time=data['list'][i]['dt_txt']
            temp=(data['list'][i]['main']['temp'])
            min_temp=(data['list'][i]['main']['temp_min'])
            max_temp=(data['list'][i]['main']['temp_max'])
            desc=(data['list'][i]['weather'][0]['description'])
            humid=(data['list'][i]['main']['humidity'])
            wind_speed=(data['list'][i]['wind']['speed'])


            print("Weather Detail of "+date_time)
            print("\n----------------------------------------------------------------------------------------------------------\n")
            print("Tempertaure: {}deg C\n".format(temp))
            print("Minimum Tempertaure: {}deg C\n".format(min_temp))
            print("Maximum Tempertaure: {}deg C\n".format(max_temp))
            print("Description: "+desc+"\n")
            print("Humidity: {}%\n".format(humid))
            print("Wind Speed: {}KMPH\n".format(wind_speed))
            print("\n----------------------------------------------------------------------------------------------------------\n")

        else:
            continue

        
