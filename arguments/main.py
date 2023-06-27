# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)


def force(mass, body='earth'):
    gravity_factors = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }

    if body.lower() in gravity_factors:
        gravity = round(gravity_factors[body.lower()], 1)
    else:
        gravity = gravity_factors['earth']

    force = mass * gravity
    return force


def pull(m1, m2, d):
    gravitational_constant = 6.674e-11
    pull = gravitational_constant * ((m1 * m2) / (d ** 2))
    return pull
