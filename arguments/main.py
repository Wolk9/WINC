# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)


def force(mass, body='earth'):
    gravity_factors = {
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'mars': 3.7,
        'jupiter': 23.1,
        'saturn': 9.0,
        'uranus': 8.7,
        'neptune': 11.0,
        'pluto': 0.7,
        'moon': 1.6
    }
    gravity = gravity_factors[body]
    force = round(mass * gravity, 1)

    return force


def pull(m1, m2, d):
    gravitational_constant = 6.674e-11
    pull = gravitational_constant * ((m1 * m2) / (d ** 2))
    return pull

