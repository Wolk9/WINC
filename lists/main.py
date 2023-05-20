# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

import operator


williams_compositions = [
    {"artist": "John Williams","year": 1973, "Title": "The Poseidon Adventure", "type": "Best Orignal Score", "status": "nominated"},
    {"artist": "John Williams","year": 1974, "Title": "Cinderella Liberty", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1974, "Title": "Tom Sawyer", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1975, "Title": "Earthquake", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1976, "Title": "Jaws", "type": "Best Original Score", "status": "Won"},
    {"artist": "John Williams","year": 1978, "Title": "Close Encounters of the Third Kind", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1978, "Title": "Star Wars: Episode IV - A New Hope", "type": "Best Original Score", "status": "Won"},
    {"artist": "John Williams","year": 1979, "Title": "Superman", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1981, "Title": "Star WArs: Episode V - The Empire Strikes Back", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1983, "Title": "E.T. the Extra Terrestrial", "type": "Best Original Score", "status": "Won"},
    {"artist": "John Williams","year": 1983, "Title": "If We Were in Love", "type": "Best Original Song", "status": "nominated"},
    {"artist": "John Williams","year": 1985, "Title": "The River", "type": "Best Original Score", "status": "nominated"},
    {"artist": "John Williams","year": 1988, "Title": "Empire of the Sun", "type": "Best Original Score", "status": "nominated"},
    {"artist": "Joseph Williams", "year": 1982, "Title": "Joseph Williams (re-released 2002)"},
    {"artist": "Joseph Williams", "year": 1996, "Title": "I Am Alive"},
    {"artist": "Joseph Williams", "year": 1997, "Title": "3"},
    {"artist": "Joseph Williams", "year": 1999, "Title": "Early Years"},
    {"artist": "Joseph Williams", "year": 2003, "Title": "Vertigo"},
    {"artist": "Joseph Williams", "year": 2006, "Title": "Two of Us"},
    {"artist": "Joseph Williams", "year": 2006, "Title": "Vertigo 2"},
    {"artist": "Joseph Williams", "year": 2007, "Title": "Smiles"},
    {"artist": "Joseph Williams", "year": 2007, "Title": "Tears"},
    {"artist": "Joseph Williams", "year": 2008, "Title": "This Fall"},
    {"artist": "Joseph Williams", "year": 2021, "Title": "Denizen Tenant"}
]



def alphabetical_order(list):
    for x in list:
        x = sorted(list, key=operator.itemgetter("Title"))
        return x



def won_golden_globe(title):
    if title == None:
        title = input("What title do you want me to check on a winning a Golden Globe? ")
    
    print("you've entered " + title);
    
    list = williams_compositions
    for x in list:
        if title.lower() in x["Title"].lower():
            if x["status"].lower() == "won":
                print(x["Title"] + ' is a winner of the Golden Globe')
                return True
            elif x["status"].lower() == "nominated":
                print(x["Title"] + ' is just nominated for a Global Globe but not a winner')
                return False
            else:
                return   
        
    return print(title + " does not match any film in my database")
    
            

def remove_toto_albums(list):
    newList = []
    for x in list:
        if "joseph" not in x["artist"].lower():
            newList.append(x)
    return newList



# print(alphabetical_order(williams_compositions))

# print(won_golden_globe("Earthquake"))
# print(won_golden_globe("Jaws"))
# print(won_golden_globe("jaws"))

print(won_golden_globe(None))

#  print(remove_toto_albums(williams_compositions))