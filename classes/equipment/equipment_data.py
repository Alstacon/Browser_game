from dataclasses import dataclass

import marshmallow

from classes.equipment.armor import Armor
from classes.equipment.weapon import Weapon


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]

    class Meta:
        unknown = marshmallow.EXCLUDE
