import json

import marshmallow.exceptions
import marshmallow_dataclass

from classes.equipment.armor import Armor
from classes.equipment.equipment_data import EquipmentData
from classes.equipment.weapon import Weapon


class Equipment:
    @staticmethod
    def _get_equipments() -> EquipmentData:
        equipment_file = open("./data/equipment.json")
        data = json.load(equipment_file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError

    def __init__(self):
        self.equipment = self._get_equipments()

    def get_weapon(self, weapon_name) -> Weapon:
        for weapon in self.equipment.weapons:
            if weapon_name == weapon.name:
                return weapon
        # return self.equipment.weapons[weapon_name]

    def get_armor(self, armor_name) -> Armor:
        for armor in self.equipment.armors:
            if armor_name == armor.name:
                return armor
        # return self.equipment.armors[armor_name]

    def get_weapon_names(self) -> list[str]:
        result = self.equipment.weapons
        return [weapon.name for weapon in result]

    def get_armor_names(self) -> list[str]:
        result = self.equipment.armors
        return [armor.name for armor in result]
