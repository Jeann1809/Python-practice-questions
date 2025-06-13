# Problem 1: Festival Lineup
def lineup(artists, set_times):
    res = {}
    for i in range(len(artists)):
        res[artists[i]] = set_times[i]
    return res

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# Problem 2: Planning App
def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, {'message': 'Artist not found'})

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

#print(get_artist_info("Blood Orange", festival_schedule)) 
#print(get_artist_info("Taylor Swift", festival_schedule))  

# Problem 3: Ticket Sales
def total_sales(ticket_sales):
    return sum(ticket_sales.values())

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

#print(total_sales(ticket_sales))

# Problem 4: Scheduling Conflict
def identify_conflicts(venue1_schedule, venue2_schedule):
    res = {}
    for key in venue1_schedule.keys(): 
        if venue1_schedule.get(key) == venue2_schedule.get(key):
            res[key]=venue1_schedule.get(key)
    return res

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))

# Problem 5: Best Set

# Use a frequency map
def best_set(votes):
    freq_map = {}
    max = 0
    winner = ""
    for artist in votes.values():
        if artist in freq_map:
            freq_map[artist] += 1
        else:
            freq_map[artist] = 1
    for artist in freq_map:
        if freq_map[artist] > max:
            max = freq_map[artist]
            winner = artist
    return winner


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "Ethel Cain",
}

#print(best_set(votes1))
#print(best_set(votes2))

# ADVANCED PROBLEMS

# Problem 1: Counting Treasure

def total_treasure(treasure_map):
    return sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

#print(total_treasure(treasure_map1)) 
#print(total_treasure(treasure_map2)) 

# Problem 2: Pirate Message Check

def can_trust_message(message):
    freq_map={}
    for character in message:
        if character.islower():
            if character in freq_map:
                freq_map[character]+=1
            else:
                freq_map[character]=1
    if len(freq_map.keys()) == 26:
        return True
    return False

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

#print(can_trust_message(message1))
#print(can_trust_message(message2))

# Problem 3: Find All Duplicate Treasure Chests in an Array
def find_duplicate_chests(chests):
    freq_map = {}
    repeats = []
    for treasure in chests:
        if treasure in freq_map:
            repeats.append(treasure)
        else:
            freq_map[treasure] = 1
    
    return repeats

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

#print(find_duplicate_chests(chests1))
#print(find_duplicate_chests(chests2))
#print(find_duplicate_chests(chests3))

# Problem 4: Booby Trap
import statistics
def is_balanced(code):
    freq_map = {}
    for char in code:
        if char in freq_map:
            freq_map[char]+=1
        else:
            freq_map[char]=1
    primary_freq = statistics.mode(freq_map.values())
    removables = []
    for char in freq_map:
        if freq_map[char] == primary_freq + 1 and len(removables) == 0:
            removables.append(char)
    if len(removables) == 1:
        return True
    else:
        return False
        


code1 = "arghh"
code2 = "hahaaahd"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
    