from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(list):
    p=10000
    for element in list:
        if len(element) < p:
            s=[element]
            p=len(element)
        elif len(element) == p:
            s.append(element)
    return s
        

def most_vowels(list):
    vowels=["A", "E", "I", "O", "U"]
    country_vowels = []
    for element in list:
        vowelcount=0
        
        for character in element:
               
            for vowel in vowels:
                if vowel.lower() == character.lower():
                    vowelcount += 1
        
        print(str(element) + ": " + str(vowelcount))
        
        country_vowels.append({"country": element, "count": vowelcount})
        
        sorted_countrys_by_number_of_vowels = sorted(country_vowels, key=lambda d: d['count'], reverse=True)
    
    
    unique_number_of_vowels = []
    for number_of_vowels in sorted_countrys_by_number_of_vowels: 
    
        if number_of_vowels["count"] not in unique_number_of_vowels:
    
            unique_number_of_vowels.append(number_of_vowels["count"])
    
    print("unique number of vowels", unique_number_of_vowels)

    top3 = range(0,3)
    top3_number_of_vowels = []
    for z in top3:
    
        for element in sorted_countrys_by_number_of_vowels:
    
            if element["count"] == unique_number_of_vowels[z]:
    
                top3_number_of_vowels.append(str(element["country"]))
            
    
    print(top3_number_of_vowels)
    
    return top3_number_of_vowels


    

def alphabet_set(countries):

    # Converteer de lijst met countries naar lowercase

    # Maak een lijst aan met letters needed
    letters_needed = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # Maak een lege lijst aan met landen die je gehad hebt
    checked_countries = []
    # Loop door alle landen heen
    
    for country in countries:
        country = country.lower()
        # print("country to check: ", country)
        for letter in country:
            # print("letter in country to check: ", letter)
            if letter in letters_needed:
                # print("the " + letter + " is in letters needed list")
                if country not in checked_countries:
                    # print("country is not yet in list of checked countries, put it in")
                    checked_countries.append(country)                    
                index = letters_needed.index(letter)
                letters_needed.pop(index)
            # else:
                #print("the " + letter + " is not in letters needed list (anymore)")
        
        # print("lijst van landen: " + str(checked_countries))
        # print("lijst van letters: " + str(letters_needed))
        # input("next: ")
    
    return checked_countries




# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

    # print(shortest_names(countries))

    print("Top 3", str(most_vowels(countries)))
    
    print(alphabet_set(countries))
