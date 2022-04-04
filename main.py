import requests
from datetime import datetime
import os

NUT_API = os.environ["NUT_KEY"]
NUT_ID = os.environ["NUT_ID"]
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUT_HEADERS = {
    "x-app-id": NUT_ID,
    "x-app-key": NUT_API
}

NUT_JSON = {
    "query": input("What did you do today?\n"),
    "gender": "male",
    "weight_kg":64,
    "height_cm":165,
    "age":30
}
nut_response = requests.post(url=NUT_ENDPOINT, headers=NUT_HEADERS, json=NUT_JSON)
nut_response.raise_for_status()
nut_data = nut_response.json()

exercise = nut_data["exercises"][0]["user_input"]
calories = nut_data["exercises"][0]["nf_calories"]
duration = nut_data["exercises"][0]["duration_min"]

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEET_JSON = {
    "workout": {
        "date": datetime.today().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}
Auth = {
    "Authorization": os.environ["TOKEN"]
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=SHEET_JSON, headers=Auth)
sheety_response.raise_for_status()

sheety_data = sheety_response.json()
print(sheety_data)



