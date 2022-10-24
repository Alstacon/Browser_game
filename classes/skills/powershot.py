import os

from classes.skills.abstract_skills import Skill


class Marksmanship(Skill):
    name = "Powershot"
    damage = 27
    stamina = 12

    def skill_effect(self) -> str:
        self.target.get_damage(self.damage)
        self.user.get_stamina_reduce(self.stamina)
        return f"""{self.user.name} выпускает невероятно точную стрелу, 
        наносящую {self.damage} урона."""


