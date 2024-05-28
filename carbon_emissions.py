import requests
import pandas as pd
class CO2Emission():
    def __init__(self):
        url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_daily_mlo.txt"
        self.data=pd.read_csv(url,sep="  ",skiprows=10000).dropna(axis=1)
        self.data.columns=['year','month','day','decimal','CO2 in ppm']
        self.data.drop(self.data.columns[[3]],axis=1,inplace=True)
    def get_latest_emission(self):
        res=self.data.tail(1).to_numpy()
        return res[0][3]
    def latest_report(self):
        res=self.data.tail(1).to_numpy()
        return f"CO2 emission on {int(res[0][2])}/{int(res[0][1])}/{int(res[0][0])} is {res[0][3]}",round(float(res[0][3]),2)
    def weekly_report(self):
        res=self.data.tail(7)
        return res.to_string(index=False),round(float(res['CO2 in ppm'].mean()),2)
    def monthly_report(self):
        res=self.data.tail(30)
        return res.to_string(index=False),round(float(res['CO2 in ppm'].mean()),2)
    def yearly_report(self):
        res=self.data.tail(12*30)
        return round(float(res['CO2 in ppm'].mean()),2)
    def get_data(self):
        return self.data