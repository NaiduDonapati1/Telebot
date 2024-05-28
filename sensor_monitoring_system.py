import random
from rules import rules
from global_variables import api_token,group_chat_id,api_key,base_url
from telegram.error import TelegramError
from telegram.error import BadRequest


#created the function for the Co2 alarm detection
class SensorMonitoring():
    
    def __init__(self,CO2):
        self.CO2=CO2
    def is_co2_voilated(self):
        #CO2 rules definition
        co2_ll = round(float(rules['co2']['LL']),2)
        co2_ul = round(float(rules['co2']['UL']),2)
        #Is CO2 read by the sensor violating the Rule defined UL or LL?
        if self.CO2 < co2_ll or self.CO2 > co2_ul:
            #print(f'CO2 Alarm : CO2 is :{co2}, Lower Limit is {co2_ll}, Uper Limit is {co2_ul}')
            return True
        else:
            #print(f'CO2 value read is :{co2}')
            return False

    def is_humidity_voilated(self,humidity):
        humidity_ll = round(float(rules['humidity']['LL']),2)
        humidity_ul = round(float(rules['humidity']['UL']),2)
        if humidity < humidity_ll or humidity > humidity_ul:
            return True
        else:
            return False
    def is_temp_voilated(self,temp):
        #CO2 rules definition
        temp_ll = round(float(rules['temp']['LL']),2)
        temp_ul = round(float(rules['temp']['UL']),2)
        #Is CO2 read by the sensor violating the Rule defined UL or LL?
        if temp < temp_ll or temp > temp_ul:
            return True
        else:
            return False