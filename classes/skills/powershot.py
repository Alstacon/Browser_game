import os

from classes.skills.abstract_skills import Skill


class Powershot(Skill):
    name = "Powershot"
    damage = 27
    stamina = 12

    def skill_effect(self) -> str:
        self.target.get_damage(self.damage)
        self.user.get_stamina_reduce(self.stamina)
        return f"""{self.user.name} заряжает лук, чтобы совершить невероятно точный и мощный выстрел
        наносящий {self.damage} урона."""


