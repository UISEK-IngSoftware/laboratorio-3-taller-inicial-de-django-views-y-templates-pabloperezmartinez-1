from django.shortcuts import render

def index(request):
    pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee", "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Gengar"]
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon_details(request, pokemon):
    return render(request, 'details.html', {'pokemon': pokemon})