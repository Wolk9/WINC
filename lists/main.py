# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

import operator

def alphabetical_order(list):
    x = sorted(list, key=operator.itemgetter("Title"))
    return [ x]

def won_golden_globe(title):
    list = john_williams_compositions
    for x in list:
        if x["Title"] == title:
            if x["status"] == "Won":
                return True
    return False
        

def remove_toto_albums(list):
    return x


john_williams_compositions = [
    {"year": 1973, "Title": "The Poseidon Adventure", "type": "Best Orignal Score", "status": "nominated"},
    {"year": 1974, "Title": "Cinderella Liberty", "type": "Best Original Score", "status": "nominated"},
    {"year": 1974, "Title": "Tom Sawyer", "type": "Best Original Score", "status": "nominated"},
    {"year": 1975, "Title": "Earthquake", "type": "Best Original Score", "status": "nominated"},
    {"year": 1976, "Title": "Jaws", "type": "Best Original Score", "status": "Won"},
    {"year": 1978, "Title": "Close Encounters of the Third Kind", "type": "Best Original Score", "status": "nominated"},
    {"year": 1978, "Title": "Star Wars: Episode IV - A New Hope", "type": "Best Original Score", "status": "Won"},
    {"year": 1979, "Title": "Superman", "type": "Best Original Score", "status": "nominated"},
    {"year": 1981, "Title": "Star WArs: Episode V - The Empire Strikes Back", "type": "Best Original Score", "status": "nominated"},
    {"year": 1983, "Title": "E.T. the Extra Terrestrial", "type": "Best Original Score", "status": "Won"},
    {"year": 1983, "Title": "If We Were in Love", "type": "Best Original Song", "status": "nominated"},
    {"year": 1985, "Title": "The River", "type": "Best Original Score", "status": "nominated"},
    {"year": 1988, "Title": "Empire of the Sun", "type": "Best Original Score", "status": "nominated"}
    ]

print(alphabetical_order(john_williams_compositions))

print(won_golden_globe("Earthquake"))
print(won_golden_globe("Jaws"))
