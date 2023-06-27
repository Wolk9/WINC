# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)


def force(mass, body='earth'):
    gravity_factors = {
        'mercury': 3.7,
        'venus': 8.87,
        'earth': 9.8,
        'mars': 3.71,
        'jupiter': 24.79,
        'saturn': 10.44,
        'uranus': 8.69,
        'neptune': 11.15,
        'pluto': 0.62,
        'moon': 1.62
    }
    
    if body.lower() in gravity_factors:
        gravity = round(gravity_factors[body.lower()], 1)
    else:
        raise ValueError("Verkeerde body naam.")
    
    force = mass * gravity
    return force



def pull(m1, m2, d):
    gravitational_constant = 6.674e-11
    pull = gravitational_constant * ((m1 * m2) / (d ** 2))
    return pull

