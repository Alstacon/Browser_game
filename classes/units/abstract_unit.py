import random
from abc import ABC, abstractmethod
from random import randint
from typing import Optional

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

    @stamina_points.setter
    def stamina_points(self, value):
        self._stamina_points = value

    @health_points.setter
    def health_points(self, value):
        self._health_points = value

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def get_damage(self, damage: float) -> None:
        self._hp -= damage
        self._hp = 0 if self._hp < 0 else self._hp



    def get_armor_damage(self, damage):
        damage = damage // 2
        self.armor.defence = round((self.armor.defence - damage), 2)
        self.armor.defence = 0 if self.armor.defence < 0 else self.armor.defence

    def get_stamina_reduce(self, stamina_cost: int):
        self._stamina -= stamina_cost
        self._stamina = 0 if self._stamina < 0 else self._stamina

    def _count_damage(self, target) -> int:
        if target.stamina_points >= 2 and target.armor.defence != 0:
            random_damage = self.unit_class.attack + round(
                random.uniform(self.weapon.min_damage, self.weapon.max_damage))
            damage = round(random_damage - target.armor.defence)
            damage = 0 if damage < 0 else damage
            target.get_armor_damage(random_damage)
            target.get_stamina_reduce(target.armor.stamina_per_turn)
        else:
            damage = round(
                self.unit_class.attack + random.uniform(self.weapon.min_damage, self.weapon.max_damage)
            )
            target.get_armor_damage(damage)
        target.get_damage(damage)
        self.get_stamina_reduce(self.weapon.stamina_per_hit)
        return damage

    @abstractmethod
    def hit(self, target) -> str:
        pass

    def use_skill(self, target) -> str:
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        if self._is_skill_used is True:
            return """Навык уже использован"""
        else:
            self._is_skill_used = True
            return self.unit_class.skill.use(user=self, target=target)
