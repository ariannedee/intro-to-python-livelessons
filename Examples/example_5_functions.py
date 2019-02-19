def add(a, b):
    return a + b


def say_hello(name, shout=False):
    if shout:
        name = name.upper()
    return 'Hello ' + name


print(say_hello('pete'))
print(say_hello('pete', True))
