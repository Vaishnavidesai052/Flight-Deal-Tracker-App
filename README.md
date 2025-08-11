Flight Deal Tracker
A Python application that tracks flight prices for various destinations and identifies cheaper flight deals compared to stored lowest prices.

Features
Fetches destination data (cities, prices, IATA codes) from a Google Sheet via the Sheety API.

Automatically fills missing IATA codes by querying flight data APIs.

Searches for the cheapest flights from a specified origin city to multiple destinations within a 6-month timeframe.

Compares current flight prices with stored lowest prices and highlights price drops.

Project Setup and Workflow
Google Sheet Setup
Created a Google Sheet with destination cities and their respective lowest acceptable prices.
Connected the sheet to the project via the Sheety API for easy data retrieval and updates.

DataManager Module
Fetches destination data from Sheety API.
Updates the Google Sheet with missing IATA airport codes after retrieving them.

Flight Search Module
Connects to the Amadeus flight search API.
Retrieves flight offers based on origin, destination, and date range.
Parses flight offers to find the cheapest available flight.

Main Application Flow
Loads destination data from Sheety.
Updates missing IATA codes.
Searches for flights over the next 6 months from origin city (default: London).
Checks if the current lowest flight price beats stored lowest prices.
Prints lower-priced flight details to console when found.

Prerequisites
Python 3.7 or higher

.env file containing:

SHEETY_USERNAME and SHEETY_PASSWORD

AMADEUS_API_KEY and AMADEUS_SECRET

How to Run
Clone the repository.

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file with the required API credentials.

Run the main script:

bash
Copy code
python main.py
Notes
Make sure your Google Sheet is correctly set up and accessible via Sheety.

API request rates are throttled with delays to avoid rate limiting.
