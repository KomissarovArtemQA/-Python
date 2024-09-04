import  requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8be07661a7dd927822eb70236184af10'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "ЧелюскинеЦ",
    "photo_id": 33
}

body_rename = {
    "pokemon_id": "67199",
    "name": "Забивзавр",
    "photo_id": 34
}

body_add = {
    "pokemon_id": "67199"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

responce_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(responce_rename.text)

responce_addpokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(responce_addpokeball.text)