from dataclasses import dataclass

from classes.skills.abstract_skills import Skill
from classes.skills.blink_strike import BlinkStrike
from classes.skills.fury_punch import FuryPunch
from classes.skills.powershot import Powershot
from classes.skills.sun_strike import SunStrike


@dataclass
class UnitClass:
    name: str
    max_hp: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


Warrior = UnitClass(name="Воин", max_hp=60, max_stamina=30, attack=0.8, stamina=0.9, armor=1.2, skill=FuryPunch())
Thief = UnitClass(name="Вор", max_hp=50, max_stamina=25, attack=1.5, stamina=1.2, armor=1.0, skill=BlinkStrike())
Wizard = UnitClass(name="Маг", max_hp=40, max_stamina=40, attack=1.2, stamina=1.2, armor=4.0, skill=SunStrike())
Elf = UnitClass(name="Эльф", max_hp=45, max_stamina=50, attack=2, stamina=1.6, armor=4.6, skill=Powershot())

unit_classes = {
    Thief.name: Thief,
    Warrior.name: Warrior,
    Wizard.name: Wizard,
    Elf.name: Elf
}