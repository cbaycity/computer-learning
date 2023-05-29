"""This file creates some helpful decorator functions for a registering the available functions on each type."""


creature_funcs = []

def creature_register(func):
    creature_funcs.append(func)
    return func

