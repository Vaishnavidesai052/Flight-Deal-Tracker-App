# import os
# import requests
# from requests.auth import HTTPBasicAuth
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0f2b567a17bef75011e5ac30d5326338/flightDeals/prices"

# class DataManager:

#     def __init__(self):
#         self._user = os.environ["SHEETY_USERNAME"]
#         self._password = os.environ["SHEETY_PASSWORD"]
#         self._authorization = HTTPBasicAuth(self._user, self._password)
#         self.destination_data = {}

#     def get_destination_data(self):
#         response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
#         data = response.json()
#         print(data)  # Debug print to verify structure
#         self.destination_data = data["prices"]
#         return self.destination_data

#     def update_destination_codes(self):
#         for city in self.destination_data:
#             new_data = {
#                 "price": {
#                     "iataCode": city["iataCode"]
#                 }
#             }
#             response = requests.put(
#                 url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
#                 json=new_data,
#                 auth=self._authorization  # Include authentication here as well
#             )
#             print(response.text)

import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        """Fetch destination data from Sheety."""
        response = requests.get(
            url=self.prices_endpoint,
            auth=self._authorization
        )
        data = response.json()
        print("DEBUG API RESPONSE:", data)  # ← Check the actual API response
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update IATA codes in the Google Sheet."""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)

    def get_customer_emails(self):
        """Fetch customer email data from Sheety."""
        response = requests.get(
            url=self.users_endpoint,
            auth=self._authorization
        )
        data = response.json()
        print("DEBUG USER RESPONSE:", data)  # ← Optional
        self.customer_data = data["users"]
        return self.customer_data
