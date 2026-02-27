import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightDataManager:
    def __init__(self):
        self.prices_endpoint = os.environ["SheetyPricesEndpointURL"]
        self.users_endpoint = os.environ["Sheety_USERS_Endpoint_URL"]
        self.username = os.environ["SheetyUserName"]
        self.password = os.environ["ShetyPassword"]

    def Get_Destination_Data(self):
        response = requests.get(
            url=self.prices_endpoint,
            auth=(self.username, self.password)
        )
        data = response.json()
        return data["prices"]
    
    def update_destination_codes(self, sheet_data):
        for row in sheet_data:
            row_id = row["id"]

            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }

            put_url = f"{self.prices_endpoint}/{row_id}"

            response = requests.put(
                url=put_url,
                json=new_data,
                auth=(self.username, self.password)
            )

            print(f"Row {row_id} Status:", response.status_code)

    def Get_Users_Data(self):
        response = requests.get(
            url=self.users_endpoint,
            auth=(self.username, self.password)
        )
        data = response.json()
        return data["users"]