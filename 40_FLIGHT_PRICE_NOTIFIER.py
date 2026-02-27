import sys
from pprint import pprint

sys.path.insert(0, r"E:\Documents_Files\RobinData\PYTHON\RawDataofpy")

from FLIGHT_DATA_MANAGER import FlightDataManager
from FLIGHT_SEARCH import FlightSearch
from FLIGHT_NOTIFICATION_MANAGER import NotificationManager

# Create objects
data_manager = FlightDataManager()
flight_search = FlightSearch()
notification = NotificationManager()

# Get data from sheet
sheet_data = data_manager.Get_Destination_Data()

# Get customer emails
customers = data_manager.Get_Users_Data()
emails = [user["email"] for user in customers]

# Ask user how to notify
while True:
    user_choice = input("Notify via (ALL / SMS / WHATSAPP / GMAIL): ").upper()

    if user_choice in ["ALL", "SMS", "WHATSAPP", "GMAIL"]:
        break
    else:
        print("Invalid option. Try again.")

# Loop through destinations
for row in sheet_data:
    destination_code = row["iataCode"]
    lowest_price = row["lowestPrice"]

    flight_data = flight_search.Search_Flight(destination_code)

    if flight_data and flight_data["price"] < lowest_price:

        # Create message based on stops
        if flight_data["stops"] == 0:
            message = (
                f"Low price alert! Only INR {flight_data['price']} "
                f"to fly from {flight_data['origin']} to {flight_data['destination']}.\n"
                f"Departure: {flight_data['out_date']}\n"
                f"Return: {flight_data['return_date']}\n"
                f"Direct Flight ✈️"
            )
        else:
            message = (
                f"Low price alert! Only INR {flight_data['price']} "
                f"to fly from {flight_data['origin']} to {flight_data['destination']}.\n"
                f"Departure: {flight_data['out_date']}\n"
                f"Return: {flight_data['return_date']}\n"
                f"{flight_data['stops']} Stop(s) Flight ✈️"
            )

        # Send notifications based on choice
        if user_choice == "ALL":
            notification.Send_sms(message)
            notification.Send_whatsapp(message)
            notification.send_emails(emails, message)

        elif user_choice == "SMS":
            notification.Send_sms(message)

        elif user_choice == "WHATSAPP":
            notification.Send_whatsapp(message)

        elif user_choice == "GMAIL":
            notification.send_emails(emails, message)