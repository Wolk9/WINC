__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowner:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.contracts = []

    def add_contract(self, specialist):
        if specialist.profession in self.needs:
            self.contracts.append(specialist.name)


class Specialist:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


class Contract:
    def __init__(self, homeowner, specialist):
        self.homeowner = homeowner
        self.specialist = specialist

    def __str__(self):
        return f"Homeowner: {self.homeowner.name}, Specialist: {self.specialist.name}"


# Create homeowners
alice = Homeowner("Alice Aliceville")
bob = Homeowner("Bob Bobsville")
craig = Homeowner("Craig Craigsville")
alfred = Homeowner("Alfred Alfredson")
bert = Homeowner("Bert Bertson")
candice = Homeowner("Candice Candicedottir")

# Create specialists
alice_profession = Specialist("Alice Aliceville", "electrician")
bob_profession = Specialist("Bob Bobsville", "painter")
craig_profession = Specialist("Craig Craigsville", "plumber")

# Set needs for homeowners
alfred.needs = ["painter", "plumber"]
bert.needs = ["plumber"]
candice.needs = ["electrician", "painter"]

# Create contracts
contracts = []

for homeowner in [alfred, bert, candice]:
    for need in homeowner.needs:
        if need == alice_profession.profession:
            homeowner.add_contract(alice_profession)
        elif need == bob_profession.profession:
            homeowner.add_contract(bob_profession)
        elif need == craig_profession.profession:
            homeowner.add_contract(craig_profession)

        # Additional logic for comparing and contracting the best offer
        if homeowner.contracts:
            best_offer = min(homeowner.contracts, key=lambda c: c.price)
            contract = Contract(homeowner, best_offer)
            contracts.append(contract)

# Print contracts
for contract in contracts:
    print(contract)
