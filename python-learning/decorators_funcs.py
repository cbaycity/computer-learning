"""This file creates some helpful decorator functions for a registering the available functions on each type."""

from typing import List, Callable, Tuple
from numbers import Number
from decorators_creatures import Creature
import copy

creature_funcs = []

damage_funcs = []

def creature_register(func):
    creature_funcs.append(func)
    return func

def damage_register(func):
    damage_funcs.append(func)
    return func

def highest_attack(funcs_list: List[Callable], attacker: Creature, target: Creature) -> Tuple[Callable, Number]:
    """This determines which attack in the list will deal the most damage to a target creature."""
    
    expected_health = target.health
    high_damage_func = lambda x : x*2
    for func in funcs_list:
        target_copy = copy.copy(target)
        func(attacker, target_copy)
        end_health = target_copy.health
        if end_health < expected_health:
            expected_health = end_health
            high_damage_func = func
    return (high_damage_func, expected_health)
