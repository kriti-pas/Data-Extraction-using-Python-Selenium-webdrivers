
Overview:

This project focuses on extracting booking data from the Abhibus platform. The data is initially in CSV format and is then converted into JSON. The project includes RESTful APIs that allow interaction with the dataset using GET and POST methods.

Project Structure:

booking.py: This script extracts booking data from the booking.csv file, sourced from Abhibus.

dataset.json: The dataset contains the booking data in JSON format.

jsonvson.py: A script used to convert the CSV file to JSON.

sleeper.py: This script loads the CSV data and converts it to JSON, saving it as dataset.json.

app.py: Implements the RESTful APIs using Flask. It provides methods to interact with the dataset, such as fetching the data (GET) and adding new booking entries (POST).

Installation and Setup:

Clone the repository using Git and navigate into the project directory.

Install the required dependencies, including pandas and Flask.

Run the conversion script to convert the CSV data to JSON.

Start the Flask server to access the APIs.

API Endpoints:

GET /api/bookings: This endpoint fetches the booking data in JSON format.
POST /api/bookings: This endpoint allows adding new booking entries to the dataset.

What I used:

After running the Flask server, you can interact with the APIs using tools like Postman. Use the GET method to fetch all booking data and the POST method to add new entries to the dataset.

