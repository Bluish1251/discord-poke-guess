import json
import re
from collections import Counter

def pokemon_name(pokename):
    if pokename == "quit": return

    pokemon_named = re.sub(r'[_\.]+', '', pokename).strip() #Splitting names for Pokemon Name

    print(pokemon_named)

    #Change path for json
    with open(r"pokemonguess\en.json", encoding='utf-8') as pokedex: pokemon_list = json.load(pokedex)
            

    input_char_counter = Counter(pokemon_named.lower())

    pokemon_guess = []

    for pokemon in pokemon_list:
        pokemon_counter = Counter(pokemon.lower())
        #Check if all characters in the input are present in the pokemon name
        if all(pokemon_counter[char] >= input_char_counter[char] for char in input_char_counter):
            pokemon_guess.append(pokemon)

    if pokemon_guess:
        print("Matched Pokémon:", pokemon_guess)
    else:
        print("No matches found.")

if __name__ == '__main__':
    user = input("Enter the Pokemon's name! [ or enter quit :>) ]")
    pokemon_name(user)