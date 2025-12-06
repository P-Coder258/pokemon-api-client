import requests

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    # Basic error check
    if response.status_code != 200:
        print(f"Error: Could not fetch data for '{name}'. Status code {response.status_code}")
        return None

    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"]
    }

if __name__ == "__main__":
    info = get_pokemon_info("pikachu")
    print(info)
