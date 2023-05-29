"""This module is used to test the decorators functions."""

import decorators_funcs as df
from numbers import Number

class Creature:
    def __init__(self) -> None:
        self.xPos = 0 # spawn at 0.
        self.attack_dmg = 1
        self.health = 10


@df.creature_register
def moveRight(creature: Creature, speed: Number):
    creature.xPos = speed + creature.xPos

@df.creature_register
def attack(attacker: Creature, target: Creature):
    target.health = target.health - attacker.attack_dmg

print("Creature Function Registry")
print(df.creature_funcs)

hero = Creature()
enemy = Creature()

attack(hero, enemy)
print("Hero attacks enemy")
print(f"Hero Health: {hero.health}, Enemy Health: {enemy.health}")