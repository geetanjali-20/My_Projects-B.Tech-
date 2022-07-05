import requests   
from datetime import datetime                #Importing libraries
import re
from urllib.request import urlopen
import json
import csv


choice=int(input("Enter your choice:\n1.Using Latitude and Longitude\n2.Using City name\n3.Using CityID\n\n"))
user_api=input("Enter your API KEY: ")        

if choice==1:
    lat=input("Enter latitude value: ")          #Input the coordinates of the location  for delhi latitude:28.6667,longitude:77.2167
    long=input("Enter longitude value: ")
    date=input("Enter date in YYYY-MM-DD) format: ")


    complete_link="https://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+long+"&units=metric&appid="+user_api

    link=requests.get(complete_link)
    data=link.json()
    #To get data in json format :-  print(data)  

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

        
elif choice==2:
    city=input("Enter city name:  ")
    complete_link="https://api.openweathermap.org/data/2.5/forecast?q="+city+"&appid="+user_api
    link=requests.get(complete_link)
    data=link.json()
    
    print("\nCity latitude: ",data['city']['coord']['lat'],", longitude: ",data['city']['coord']['lon'],"\n\n")   #To get coordintes of the entered city
    #print(data)

elif choice==3:
    cityID=input("Enter CityID:  ")
    complete_link="https://api.openweathermap.org/data/2.5/forecast?id="+cityID+"&appid="+user_api
    link=requests.get(complete_link)
    data=link.json()
    
    print("\nCity latitude: ",data['city']['coord']['lat'],", longitude: ",data['city']['coord']['lon'],"\n\n")  #To get coordintes of the entered city
    #print(data)

    
    

#Pass url 

# url = "https://api.openweathermap.org/data/2.5/forecast?q=Delhi&appid=c8323e69ca0457522bf3ca314b66890f"  

response = urlopen(complete_link)

data_json = json.loads(response.read())


out_file = open("myfile.json", "w") 
    
json.dump(data_json, out_file, indent = 6) 
    
out_file.close()

with open("myfile.json") as json_file:
	jsondata = json.load(json_file)
    

data_file = open("jsonoutput.csv", 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for j in jsondata:
    if count == 0:
        header = jsondata.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(jsondata.values())

data_file.close()




    
    
    
