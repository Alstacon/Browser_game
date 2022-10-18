from dataclasses import dataclass

from classes.skills.abstract_skills import Skill
from classes.skills.blink_strike import BlinkStrike
from classes.skills.fury_punch import FuryPunch


@dataclass
class UnitClass:
    name: str
    max_hp: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


Warrior = UnitClass(name="Воин", max_hp=600, max_stamina=300, attack=8, stamina=9, armor=12, skill=FuryPunch())
Thief = UnitClass(name="Вор", max_hp=500, max_stamina=250, attack=15, stamina=12, armor=10, skill=BlinkStrike())

unit_classes = {
    Thief.name: Thief,
    Warrior.name: Warrior
}