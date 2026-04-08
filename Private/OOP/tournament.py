#!/bin/python

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from random import randint

class Warrior(ABC):

# Init

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.__hp = hp
        self.__max_hp = hp
        self.attack = attack
        self.defence = defence

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = max(0, min(value, self.__max_hp))

    @property
    def max_hp(self):
        return self.__max_hp

    def __str__(self):
        return f"My name is {self.name} and my HP is equal to {self.hp}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, hp={self.hp}, attack={self.attack}, defence={self.defence})"
# abstract methods

    @abstractmethod    
    def special_skill(self, target):
        pass

    @abstractmethod
    def desc(self):
        pass

# Combat methods

    def take_damage(self, dmg):
        effective_damage = max(1, dmg - self.defence)
        self.hp = self.hp - effective_damage
        return effective_damage

    def is_alive(self):
        return self.hp > 0

# random generator

    @classmethod
    def create_random(cls):
        pass

class Knight(Warrior):
    def __init__(self, name, hp, attack, defence):
        super().__init__(name, hp, attack, defence)
        self.block_next = False
        self.shields = 3

# Combat methods

    def special_skill(self, target):
        # target unused - Knight only affects himself
        if self.shields > 0:
            self.block_next = True
            self.shields -= 1
            return f"{self.name} rises his shield - next attack will be blocked!"
        else:
            return f"{self.name} have no shields left!"

    def take_damage(self, dmg):
        if self.block_next:
            self.block_next = False
            return 0  # blocked!
        return super().take_damage(dmg)

    def desc(self):
        return "Knight is a tough warrior with shield - high HP, medium DMG"

    # random
    @classmethod
    def create_random(cls):
        name = "John Knight"
        hp = randint(40, 200)
        attack = randint(7, 20)
        defence = randint(8, 25)
        return cls(name, hp, attack, defence)

class Mage(Warrior):
    def __init__(self, name, hp, attack, defence, mana):
        super().__init__(name, hp, attack, defence)
        self.mana = mana
        self.__max_mana = mana

    @property
    def max_mana(self):
        return self.__max_mana

    def special_skill(self, target):
        # Power Word Kill
        if self.mana >= (self.__max_mana * 0.25):
            self.mana -= self.__max_mana * 0.25
            target.take_damage(self.attack * 4)
            return f"{self.name} casts Power Word Kill targeting {target.name}. It deals {self.attack * 4} DMG"
        else:
            return f"Not enough MANA: Power Word Kill needs {self.__max_mana * 0.7} MANA"
        
    def desc(self):
        return "Mage is very magickal person - low HP, high DMG"

    @classmethod
    def create_random(cls):
        name = "John Mage"
        hp = randint(70, 140)
        attack = randint(15, 30)
        defence = randint(1, 7)
        mana = randint(400, 600)
        return cls(name, hp, attack, defence, mana)

class Rogue(Warrior):
    def __init__(self, name, hp, attack, defence):
        super().__init__(name, hp, attack, defence)
        self.invisible = False

    def special_skill(self, target):
        # target unused - Rogue only affects himself
        self.invisible = True
        return f"{self.name} is invisible"
    
    def take_damage(self, dmg):
        if self.invisible:
            self.invisible = False
            return dmg * 0.7  # dodged
        return super().take_damage(dmg)

    def desc(self):
        return "Master of shadow - medium HP, medium DMG"

    @classmethod
    def create_random(cls):
        name = "John Rogue"
        hp = randint(80, 150)
        attack = randint(10, 25)
        defence = randint(5, 15)
        return cls(name, hp, attack, defence)

class Arena:
    def __init__(self, warrior1, warrior2):
        self.warrior1 = warrior1
        self.warrior2 = warrior2
        self.turns = 0

    def fight(self):
        while (self.warrior1.is_alive() and self.warrior2.is_alive()):
            self.turns += 1

            if self.turns % 3 == 0:
                print(self.warrior1.special_skill(self.warrior2))
                if not self.warrior2.is_alive():
                    break

                print(self.warrior2.special_skill(self.warrior1))
                if not self.warrior1.is_alive():
                    break

            print(f"{self.warrior1.name} attacks {self.warrior2.name} for {self.warrior1.attack}, {self.warrior2.name} takes {self.warrior2.take_damage(self.warrior1.attack)}")
            
            if not self.warrior2.is_alive():
                break

            print(f"{self.warrior2.name} attacks {self.warrior1.name} for {self.warrior2.attack}, {self.warrior1.name} takes {self.warrior1.take_damage(self.warrior2.attack)}")

            if not self.warrior1.is_alive():
                break

        winner = self.warrior1 if self.warrior1.is_alive() else self.warrior2
        print(f"\nWinner: {winner.name} after {self.turns} turns!")
        return winner

    def __len__(self):
        return self.turns
    
    @staticmethod
    def tldr():
        return "Two warriors, each of whom can use their special ability once every 3 turns."

@dataclass
class Statistics:
    wins: dict = field(default_factory=dict)
    total_damage: int = 0
    total_turns: int = 0

    def save_results(self, winner, turns):
        if winner.name in self.wins:
            self.wins[winner.name] += 1
        else:
            self.wins[winner.name] = 1
        self.total_turns += turns

class Tournament:
    def __init__(self, warriors):
        self.warriors = warriors
        self.stats = Statistics()
    
    def start_tournament(self):
        current_round = self.warriors

        while len(current_round) > 1:
            next_round = []

            for i in range(0, len(current_round), 2):
                if i + 1 >= len(current_round):
                    next_round.append(current_round[i])
                    continue
                warrior1 = current_round[i]
                warrior2 = current_round[i + 1]
                arena = Arena(warrior1=warrior1, warrior2=warrior2)
                winner = arena.fight()
                turns = len(arena)
                self.stats.save_results(winner, turns)
                next_round.append(winner)

            current_round = next_round

        print(f"\nThe master of all is: {current_round[0].name} in {self.stats.total_turns}")
