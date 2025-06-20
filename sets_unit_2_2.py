# SETS STANDARD PROBLEMS

# Problem 1: Most Endangered Species
def most_endangered(species_list):
    min = {"name":species_list[0].get('name'),"population": species_list[0].get('population')}
    for animal in species_list:
        if animal.get('population') < min.get('population'):
            min["name"] = animal.get('name')
            min["population"] = animal.get('population')
    return min.get('name')

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

# print(most_endangered(species_list))

# Problem 2: Identifying Endangered Species
def count_endangered_species(endangered_species, observed_species):
    e_species = {}
    for specie in endangered_species:
        e_species[specie] = 0

    for specie in observed_species:
        if specie in e_species:
            e_species[specie] += 1
    
    return sum(e_species.values())

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

#print(count_endangered_species(endangered_species1, observed_species1)) 
#print(count_endangered_species(endangered_species2, observed_species2))  

# Problem 3: Navigating the Research Station

def navigate_research_station(station_layout, observations):
    index = {ch: i for i, ch in enumerate(station_layout)}
    pos = 0
    time = 0
    for ch in observations:
        time += abs(index[ch] - pos)
        pos = index[ch]
    return time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  # Output: 45
print(navigate_research_station(station_layout2, observations2))  # Output: 4
