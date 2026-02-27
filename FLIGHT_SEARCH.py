import requests
import os
from dotenv import load_dotenv
from datetime import datetime , timedelta

load_dotenv(r"E:\Documents_Files\RobinData\PYTHON\RawDataofENV\FLIGHT_BOOKING.env")

class FlightSearch:

    def __init__(self):
        self.api_key = os.environ["AMADEUS_API_KEY"]
        self.api_secret = os.environ["AMADEUS_SECRET"]
        self.token = self._get_token()

    def _get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print("Token Error:", response.text)
            return None

    def Get_IATA_Code(self, City_Name):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        params = {
            "keyword": City_Name,
            "max": 1
        }

        URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        response = requests.get(URL, headers=headers, params=params)

        if response.status_code == 200:
            try:
                return response.json()["data"][0]["iataCode"]
            except (IndexError, KeyError):
                print(f"IATA not found for {City_Name}")
                return None
        else:
            print("IATA API Error:", response.text)
            return None

    def Get_Date_Range(self):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_later = datetime.now() + timedelta(days=180)

        Departure_Date = tomorrow.strftime("%Y-%m-%d")
        Return_Date = six_month_later.strftime("%Y-%m-%d")

        return Departure_Date , Return_Date

    def Search_Flight(self,Destination_code,is_direct=True):
        departure_date, return_date = self.Get_Date_Range()
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        non_stop_value = "true" if is_direct else "false"

        Headers = {
            "Authorization": f"Bearer {self.token}"
            }
        Params = {
            "originLocationCode": "DEL",
            "destinationLocationCode": Destination_code,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": non_stop_value,
            "currencyCode": "INR",
            "max": 10
            }

        response = requests.get(url=url, headers=Headers, params=Params)

        if response.status_code != 200:
            print("Flight Search Error:", response.text)
            return None

        Data = response.json().get("data", [])

        if not Data:
            if is_direct:
                print("No direct flights found. Searching indirect flights...")
                return self.Search_Flight(Destination_code, is_direct=False)
            else:
                print("No indirect flights found either.")
                return None

        prices = []

        for flight in Data:
            price = float(flight["price"]["total"])
            prices.append(price)
        print("All Prices:", prices)

        cheapest_price = min(prices)
        print("Cheapest Price:", cheapest_price)

        for flight in Data:
            if float(flight["price"]["total"]) == cheapest_price:
                cheapest_flight = flight
                break

        segments = cheapest_flight["itineraries"][0]["segments"]
        outbound = segments[0]
        return_seg = cheapest_flight["itineraries"][1]["segments"][0]

        origin = outbound["departure"]["iataCode"]
        destination = segments[-1]["arrival"]["iataCode"]

        out_date = outbound["departure"]["at"].split("T")[0]
        return_date = return_seg["departure"]["at"].split("T")[0]
        Stops = len(segments) - 1
        return {
            "price": cheapest_price,
            "origin": origin,
            "destination": destination,
            "out_date": out_date,
            "return_date": return_date,
            "stops":Stops
        }