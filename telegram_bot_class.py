#from telegram import Bot
from global_variables import api_token,group_chat_id,api_key,base_url
import telebot
from carbon_emissions import CO2Emission
from weather_report import WeatherReport
import sensor_monitoring_system as sms
#Please install the telegram module
#pip install telegram
bot=0
sensor=0
class Telegram_Module():
    '''
      Steps to create Bot

      1. Import the Bot class from telegram module.
      2. create an instance of the Telegram bot by passing to the 
         Bot constructor method the API ID which you have created in telegram.
      3. Using this BOT instance call the send_test_message function and invoke it
         with the Telegram Group chat ID. The group has already been created by you.
    
    '''
    global bot,CO2,sensor
    bot=telebot.TeleBot(api_token)
    CO2=CO2Emission()
    sensor=sms.SensorMonitoring(CO2.get_latest_emission())
    #async def send_test_message(self, message):
        
        #Create an instance of the Telegram Bot class
       # bot = Bot(token=self.bot_token)#you need to the pass the BOT token ID
       # await bot.send_message(chat_id=group_chat_id, text=message)
    @bot.message_handler(commands=["hai","hello","hi"])
    def send_greetings(msg):
        bot.send_message(msg.chat.id,text="Hai, Hope you doing well!")
        bot.send_message(msg.chat.id,text="Select your Choice.\n1./CO2 Emission\n2./Weather Report")
    @bot.message_handler(commands=["CO2"])
    def send_CO2_menu(msg):
        if sensor.is_co2_voilated():
            bot.send_message(msg.chat.id,text=f"Alert:CO2 levels violated. CO2 level is {CO2.get_latest_emission()}")
        bot.send_message(msg.chat.id,text="Want to know CO2 emission rate.\n1./latest\n2./weekly\n3./monthly\n4./yearly\n5./exit")
    @bot.message_handler(commands=["Weather"])
    def send_weather_menu(msg):
        bot.send_message(msg.chat.id,text="Select City :\n1./hyderabad\n2./bangalore\n3./chennai\n4./delhi")
    @bot.message_handler(commands=['hyderabad','chennai','bangalore','delhi'])
    def send_weather_report(msg):
        wt=WeatherReport()
        res,temp,humidity=wt.get_report(msg.text[1:].split('@')[0])
        bot.send_message(msg.chat.id,text=res)
        if sensor.is_humidity_voilated(humidity):
            bot.send_message(msg.chat.id,text=f'Alert:Humidity levels violated.')
        if sensor.is_temp_voilated(temp):
            bot.send_message(msg.chat.id,text=f'Alert:Temperature levels violated.')
    @bot.message_handler(commands=["exit"])
    def send_exit_msg(msg):
        bot.send_message(msg.chat.id,text="Thank you for your Time")
    @bot.message_handler(commands=["latest"])
    def send_latest_report(msg):
        txt,avg=CO2.latest_report()
        bot.send_message(msg.chat.id,text=txt)
        if sensor.is_co2_voilated():
            bot.send_message(msg.chat.id,text="Alert:CO2 levels violated")
    @bot.message_handler(commands=["weekly"])
    def send_weekly_report(msg):
        txt,avg=CO2.weekly_report()
        bot.send_message(msg.chat.id,text=txt)
        bot.send_message(msg.chat.id,text=f"average CO2 emission for last week is {avg}")
    @bot.message_handler(commands=["monthly"])
    def send_monthly_report(msg):
        txt,avg=CO2.monthly_report()
        bot.send_message(msg.chat.id,text=txt)
        bot.send_message(msg.chat.id,text=f"average CO2 emission for last month is {avg}")
    @bot.message_handler(commands=["yearly"])
    def send_yearly_report(msg):
        avg=CO2.yearly_report()
        #bot.send_message(msg.chat.id,text=txt)
        bot.send_message(msg.chat.id,text=f"average CO2 emission for last year is {avg}")
    @bot.message_handler(commands=["menu"])
    def send_menu(msg):
        bot.send_message(msg.chat.id,text="Select your Choice.\n1./CO2 Emission\n2./Weather Report")
    @bot.message_handler(func=lambda msg:True)
    def other_msg(msg):
        bot.send_message(msg.chat.id,text="Invalid message")
        bot.send_message(msg.chat.id,text="Select your Choice.\n1./CO2 Emission\n2./Weather Report")
    bot.infinity_polling()
