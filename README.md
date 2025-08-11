Flight Deal Tracker App ✈️💸
Overview
A Python-based automation tool that monitors flight prices for specified destinations and alerts users when ticket prices drop below a defined threshold.
Built as part of the 100 Days of Code – Python Pro Bootcamp course, this project combines API integration, data management, and automated notifications to deliver real-time flight deal tracking.

Features
Price Monitoring: Continuously checks flight prices using the Kiwi Tequila API.

Google Sheets Integration: Stores and updates flight search data using the Sheety API for easy editing and tracking.

User Notifications: Sends alerts via email/SMS when flight prices fall below the target value.

Dynamic Search: Automatically updates IATA codes for destinations and retrieves the cheapest flights available.

Customizable: Users can set preferred destinations and budget limits directly in Google Sheets.

Tech Stack & Tools
Language: Python

APIs:

Tequila API (Kiwi) – Flight search and pricing data

Sheety API – Google Sheets integration

Twilio API / SMTP – SMS/Email alerts

Libraries: requests, datetime, smtplib, twilio

Data Storage: Google Sheets (via Sheety API)

How It Works
Destination Setup: Add your preferred cities and price limits to the linked Google Sheet.

IATA Code Fetching: The app retrieves IATA airport codes for your destinations if not already set.

Flight Search: Checks for the cheapest flights from your origin city to each listed destination.

Alerts: If a price is lower than your threshold, sends an email/SMS with trip details and booking link.

Learning Outcomes
API integration and authentication

Data retrieval and JSON parsing

Working with external services like Google Sheets & Twilio

Automating workflows using Python

Sending automated alerts via email and SMS

Future Improvements
Deploy on AWS Lambda or EC2 for continuous background execution

Add a web-based dashboard for real-time flight tracking

Support for multiple origin airports and date ranges
