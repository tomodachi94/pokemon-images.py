import random

POKEMON_TOTAL = 1008 # Increment this as more Pokemon are added

def get_url_from_number(image_number: int):
    """Gets a Pokemon image URL from an image number."""
    padded: str

    if len(str(image_number)) == 1:
        padded = f"{image_number:02d}"
    elif len(str(image_number)) == 2:
        padded = f"{image_number:01d}"
    elif len(str(image_number)) == 3:
        padded = str(image_number)
    elif len(str(image_number)) == 4:
        padded = str(image_number)
    else:
        padded = ""

    return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{padded}.png"


def get_random_url():                           
    """Gets a random Pokemon image's URL."""
    image_number = random.randint(1, POKEMON_TOTAL)

    return get_url_from_number(image_number)

