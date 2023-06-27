    def count_unique_joey_facts():
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
