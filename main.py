# Import libs
import scratchattach as scratch3
import requests

# Define session and connection vars
session = scratch3.Session("sessionID", username="BusyBird15")  # replace with your session_id and username
conn = session.connect_cloud("XXXXXXXXX")  # replace with your project id

# Connect to Scratch
client = scratch3.CloudRequests(conn)


@client.request
def getData(location):  # called when client receives request
    print("Weather request received")
    response = requests.get("https://api.weatherapi.com/v1/forecast.json?key=XXXXXXXXXXXXX&q=" + location + "&days=3") # Replace "XXXXXXX" with your weatherapi.com token
    if response.status_code == 400:
        return ["NON-FATAL ERROR: 400, LOCATION NOT FOUND"]
    elif response.status_code == 401:
        print("FATAL WARNING: API limit reached!")
        return ["FATAL ERROR: 400, API CALL LIMIT"]

    elif response.status_code == 200:
        location = response.json()['location']
        current = response.json()['current']
        condition = current['condition']
        return [location['name'], location['region'], location['country'], condition['text'], current['temp_f'], current['humidity'], current['temp_c']] #sends back to the Scratch project


@client.request
def getAlerts(location):
    print("Alert request received")
    response = requests.get("https://api.weatherapi.com/v1/forecast.json?key=XXXXXXXXXX&q=" + location + "&days=3") # Replace "XXXXXXX" with your weatherapi.com token
    if response.status_code == 401:
        print("FATAL WARNING: API limit reached!")
        return ["FATAL ERROR: 400, API CALL LIMIT"]
    elif response.status_code == 200:
        return ["THIS IS A TEST ALERT; ALERTS DO NOT FUNCTION YET"]

@client.event
def on_ready():
    print("Request handler is running...")


client.run()
