from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle', 'Jigglypuff', 'Meowth', 'Psyduck', 'Snorlax']
    return render(request, 'index.html', {
        'pokemons': pokemons
    })

def pokemon_details(request, pokemon):
    return render(request, 'details.html', {
        'pokemon': pokemon
    })