import os
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv

load_dotenv(r"E:\Documents_Files\RobinData\PYTHON\RawDataofENV\FLIGHT_BOOKING.env")

class NotificationManager:
    def __init__(self):
        self.sid = os.environ["SID"]
        self.auth_token = os.environ["Auth_tokens"]
        self.twilio_SMS_number = os.environ["Twilio_SMS_No"]
        self.my_SMS_number = os.environ["My_SMS"]

        self.my_whatsapp_number = os.environ["My_Whatsapp"]
        self.twilio_whatsapp_number = os.environ["Twilio_WhatsApp_No"]

        self.gmail = os.environ["User_Gmail"]
        self.gmail_password = os.environ["User_Password"]

        self.client = Client(self.sid, self.auth_token)
        
    def Send_sms(self,message):
        self.client.messages.create(
            body=message,
            from_=self.twilio_SMS_number,
            to=self.my_SMS_number
        )

    def Send_whatsapp(self,message):
        self.client.messages.create(
            body=message,
            from_=self.twilio_whatsapp_number,
            to=self.my_whatsapp_number
        )

    def Send_gmail(self,message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(
                user=self.gmail, 
                password=self.gmail_password
                )
            connection.sendmail(
                from_addr=self.gmail,
                to_addrs=self.gmail,
                msg=(f"Your FlightDetails\n\n{message}")
                )

            