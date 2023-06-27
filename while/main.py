from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# number = 0

def unique_koala_facts(number):
    unique_koala_facts = []
    iteration_limit = 1000
    iterations = 0

    while number > 0 and iterations < iteration_limit:
        koala_fact = random_koala_fact()
        iterations += 1

        if koala_fact not in unique_koala_facts:
            unique_koala_facts.append(koala_fact)
            number -= 1

    # print("We hebben nu", len(unique_koala_facts), "unieke koala feiten")
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


def koala_weight():
    weight_fact = random_koala_fact()

    # Zoek naar het feit over het gewicht in de vorm van "Het gewicht van een koala is X pond."
    # Pas deze code aan als de indeling van het feit varieert.
    while "pounds" not in weight_fact:
        weight_fact = random_koala_fact()

    # Haal de waarde van het gewicht uit het feit
    weight_in_pounds = int(weight_fact.split(" ")[-2])

    # Converteer ponden naar kilogram (1 pond = 0.453592 kg)
    weight_in_kg = round(weight_in_pounds * 0.453592)

    return weight_in_kg

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.


if __name__ == "__main__":
    unique_koala_facts()
    koala_weight()
