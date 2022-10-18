from abc import ABC, abstractmethod
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
        self._is_skill_used = None

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

    def _count_damage(self, target) -> int:
        if target.stamina >= 10:
            damage = self.unit_class.attack - target.armor
            target.stamina -= 10
        else:
            damage = self.unit_class.attack
        target.self.get_damage(damage)
        target.armor -= damage
        self.stamina -= 20
        return damage

    def get_damage(self, damage: int) -> Optional[int]:
        self.hp -= damage
        return round(self.hp)


    @abstractmethod
    def hit(self, target) -> str:
        """
        этот метод будет переопределен ниже
        """
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
        if self._is_skill_used:
            return """Навык уже использован"""
        else:
            self.unit_class.skill.use(user=self, target=target)

