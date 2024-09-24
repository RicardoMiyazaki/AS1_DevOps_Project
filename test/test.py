from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio


def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}


city = input("Digite a Cidade: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)

