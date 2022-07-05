import tkinter as tk
import requests
import time
import re


def getWeather(canvas):
        lat= textField.get()        #Input the coordinates of the location
        long=textField.get()
        date=textField.get()
        user_api=textField.get()
        
        complete_link="https://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+long+"&units=metric&appid="+user_api+";

        link=requests.get(complete_link)
        data=link.json() 

    
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

            else:
                continue

    
        final_info = desc + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n"  +"Humidity: " + str(humid) + "\n" +"Wind Speed: " + str(wind_speed)
        label1.config(text = final_info)
        label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
