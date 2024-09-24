import app
import requests
from pprint import pprint

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


API_Key = 'dab2e4d2d099b06d753e139496a2fb05'

city = input("Digite a Cidade: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)

