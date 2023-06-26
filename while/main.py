from helpers import random_koala_fact
import time 

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"
number = 0

def unique_koala_facts(number):
    unique_koala_facts = []
    unique_koala_facts_numbered = []
    
    
    while number > 0:
        koala_fact = random_koala_fact();    
        if koala_fact not in unique_koala_facts:
            print(number, " ", koala_fact, " staat er nog niet in!")
            unique_koala_facts.append(koala_fact)
            #time.sleep(1)
        else:
            index = unique_koala_facts.index(koala_fact)
            #time.sleep(0.5)
            print(koala_fact, "\nstaat er in op index: ", str(index) )
        print("\nnumber: ", number)
        print("list: ", unique_koala_facts, "\n\n")
        number += -1
     

    
    #unique_koala_facts.sort()
    print("we hebben nu ", len(unique_koala_facts), " unieke koala feiten")
    return unique_koala_facts

def num_joey_facts():
    koala_facts_with_joey = []
    unique_koala_facts = []
    fact = 0
    number = 1000
    

    while number > 0:
        koala_fact = random_koala_fact();
        if koala_fact not in koala_facts_with_joey:
            if "joeys" in koala_fact:
                koala_facts_with_joey.apped(koala_fact)
            else:
                fact += 1    
        else:
            number -= 1



    return num_joey_facts

def koala_weight():
    return koala_weight


    

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    
    print(unique_koala_facts(1000))
