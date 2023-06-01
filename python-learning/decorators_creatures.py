"""This module contains classes for the decorators tutorial. Notably the creatures class."""

class Creature:
    """This class creates creatures that can target and damage each other."""
    def __init__(self) -> None:
        self.xPos = 0 # spawn at 0.
        self.attack_dmg = 1
        self.health = 10
        self.super_attack = 10

