import sys
print(sys.version)
print(sys.executable)


def greet(greetme):
    greeting = 'Hello, {}'.format(greetme)
    return greeting


print(greet('World'))
print(greet('Kris'))
