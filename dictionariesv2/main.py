# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }
    return passport


def add_stamp(passport, country):
    # Check of 'stamps' key bestaat in de passport dictionary
    if 'stamps' not in passport:
        passport['stamps'] = []

    # Check of het land niet het thuisland van de person is en geen dubbele stempel
    if country != passport['nationality'] and country not in passport['stamps']:
        passport['stamps'].append(country)

    return passport


def add_biometric_data(passport, name, value, date):
    # Check of het paspoort al biometrische data heeft
    if 'biometric' not in passport:
        passport['biometric'] = {}

    # Check of de specifieke biometrische data al bestaat in het paspoort
    if name not in passport['biometric']:
        passport['biometric'][name] = {}

    # Update de waarde en datum van de biometrische data
    passport['biometric'][name]['value'] = value
    passport['biometric'][name]['date'] = date

    return passport

