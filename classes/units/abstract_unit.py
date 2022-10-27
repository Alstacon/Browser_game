import random
from abc import ABC, abstractmethod

from classes.equipment.armor import Armor
from classes.equipment.weapon import Weapon
from classes.units.units import UnitClass


class BaseUnit(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self._hp = unit_class.max_hp
        self._stamina = unit_class.max_stamina
        self.weapon = None
        self.armor = None
        self._is_skill_used = False

    @property
    def health_points(self):
        return self._hp

    @property
    def stamina_points(self):
        return self._stamina

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def get_damage(self, damage: float) -> None:
        self._hp = round(self._hp - damage, 2)
        self._hp = 0 if self._hp < 0 else self._hp

    def get_damage_reduce(self, damage):
        armor = self.armor.defence * self.unit_class.armor
        damage = round(damage - armor, 2)
        damage = 0 if damage < 0 else damage
        return damage

    def get_stamina_reduce(self, stamina_cost: int):
        self._stamina = round(self._stamina - stamina_cost, 2)
        self._stamina = 0 if self._stamina < 0 else self._stamina

    def _count_damage(self, target) -> int:
        if target.stamina_points >= 2:
            damage = self.unit_class.attack * random.uniform(self.weapon.min_damage, self.weapon.max_damage)
            final_damage = self.get_damage_reduce(damage)
            target.get_stamina_reduce(target.armor.stamina_per_turn)
        else:
            final_damage = self.unit_class.attack * random.uniform(self.weapon.min_damage, self.weapon.max_damage)
        target.get_damage(final_damage)
        self.get_stamina_reduce(self.weapon.stamina_per_hit)
        return final_damage

    @abstractmethod
    def hit(self, target) -> str:
        pass

    def use_skill(self, target) -> str:
        if self._is_skill_used is True:
            return """Навык уже использован"""
        else:
            self._is_skill_used = True
            return self.unit_class.skill.use(user=self, target=target)
