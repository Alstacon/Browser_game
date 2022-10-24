from classes.arena.arena import Arena
from classes.equipment.equipment import Equipment
from classes.units.units import unit_classes

arena = Arena()

heroes = {}

equipment = Equipment()

char_information = {
    'classes': unit_classes,
    'weapons': equipment.get_weapon_names(),
    'armors': equipment.get_armor_names(),
}
