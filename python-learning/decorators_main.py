"""This module is used to test the decorators functions."""

import decorators_funcs as df
from numbers import Number
from decorators_creatures import Creature


@df.creature_register
def moveRight(creature: Creature, speed: Number):
    creature.xPos = speed + creature.xPos

@df.creature_register
@df.damage_register
def attack(attacker: Creature, target: Creature):
    target.health = target.health - attacker.attack_dmg

@df.creature_register
@df.damage_register
def super_attack(attacker: Creature, target: Creature):
    target.health = target.health - attacker.super_attack

print("Creature Function Registry")
print(df.creature_funcs)

hero = Creature()
enemy = Creature()

attack(hero, enemy)
print("Hero attacks enemy")
print(f"Hero Health: {hero.health}, Enemy Health: {enemy.health}")

print("Best Attack:")
print(df.highest_attack(df.damage_funcs, hero, enemy))