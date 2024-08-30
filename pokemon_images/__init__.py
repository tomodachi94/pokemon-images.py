import random

POKEMON_TOTAL = 1025 # Increment this as more Pokemon are added

def get_url_from_number(image_number: int):
    """Gets a Pokemon image URL from an image number."""
    padded: str

    image_number = str(image_number)

    if len(image_number) == 1:
        padded = "00" + image_number
    elif len(image_number) == 2:
        padded = "0" + image_number
    elif len(image_number) == 3:
        padded = image_number
    elif len(image_number) == 4:
        padded = image_number
    else:
        raise ValueError

    return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{padded}.png"


def get_random_url():                           
    """Gets a random Pokemon image's URL."""
    image_number = random.randint(1, POKEMON_TOTAL)

    return get_url_from_number(image_number)

