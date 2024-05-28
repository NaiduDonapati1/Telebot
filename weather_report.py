import requests, json
from global_variables import api_key,base_url
class WeatherReport():
    def get_report(self,city):
        complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = round(float(y["temp"]-273.15),2)
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            res=f" Temperature  is {current_temperature} ℃ \n atmospheric pressure is {current_pressure} hPa\n humidity  is {current_humidity}⁒\n {weather_description}"
            return res,current_temperature,current_humidity
        else:
            return " City Not Found ",0,0
# wt=WeatherReport()
# n=input("enter city name : ")
# print(wt.get_report(n))
            