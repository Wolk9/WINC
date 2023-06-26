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
    unique_joey_facts = set()
    fact_counts = {}

    while True:
        random_fact = random_koala_fact()

        if random_fact in fact_counts:
            fact_counts[random_fact] += 1
        else:
            fact_counts[random_fact] = 1

        # Check if a fact has been seen 10 times
        if fact_counts[random_fact] == 10:
            break

        if 'joey' in random_fact:
            unique_joey_facts.add(random_fact)

    return len(unique_joey_facts)

    unique_joey_count = count_unique_joey_facts()
    print("Number of unique facts mentioning 'joey':", unique_joey_count)  

    unique_joey_count = num_joey_facts

    return num_joey_facts

def koala_weight():
    return koala_weight


    

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    
   # print(unique_koala_facts(1000))
    print(num_joey_facts())