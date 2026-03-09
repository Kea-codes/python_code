# CONNECTING TO THE API USING PYTHON
# THERE WAS NO requests LIBRARY , I HAD TO DOWNLOAD IT
# USING pip install requests IN THE VSCODE BUILT IN TERMINAL


import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data =response.json()
        return pokemon_data
    else:
        print(f"faild to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    print(f"weight: {pokemon_info["weight"]}")