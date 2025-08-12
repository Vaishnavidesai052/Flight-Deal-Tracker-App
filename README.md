✈️ Flight Deal Tracker
A Python application that tracks flight prices for destinations and alerts you when cheaper deals are found.

🚀 Features
📋 Fetches destination data from Google Sheet via Sheety API

🛫 Fills missing IATA codes using flight data APIs

🔍 Searches for the cheapest flights from a specified origin city over 6 months

💸 Compares prices with stored lowest prices and highlights price drops

📄 Google Sheet & Form
Create a Google Sheet with columns: City, IATA Code, Lowest Price
Link it to this Google Form for easy data entry:
📝 Fill the Google Form

🧩 Modules
📊 DataManager – Fetches data and updates missing IATA codes

🛩 Flight Search – Uses Amadeus API to find cheapest flights

⚙️ Requirements
🐍 Python 3.7+

.env file containing:

SHEETY_USERNAME, SHEETY_PASSWORD

AMADEUS_API_KEY, AMADEUS_SECRET

▶️ How to Run
📥 Clone the repository

📦 Install dependencies:

bash
Copy code
pip install -r requirements.txt
🛠 Create .env with credentials

🏃 Run:

bash
Copy code
python main.py
If you want, I can also make 
