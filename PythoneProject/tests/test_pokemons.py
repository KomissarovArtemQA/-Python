import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8be07661a7dd927822eb70236184af10'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 5325

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_nametrainer_from_responce():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert  response.json()["data"][0]["trainer_name"] == 'Потапыч' 


