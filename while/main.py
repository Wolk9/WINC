from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number):
    unique_koala_facts = []
    
    while number > 0:
        koala_fact = random_koala_fact();    
        if koala_fact not in unique_koala_facts:
            print(koala_fact + " staat er nog niet in!")
            unique_koala_facts.append(koala_fact)
        else:
            print("staat er in")
        number += -1
        print(number)

    
    unique_koala_facts.sort()
    print(len(unique_koala_facts))
    return unique_koala_facts

def num_joey_facts(number):
    return num_joey_facts

def koala_weight(number):
    return koala_weight


    

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    
    print(unique_koala_facts(15000))
