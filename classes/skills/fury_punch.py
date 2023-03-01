import os

from classes.skills.abstract_skills import Skill


class FuryPunch(Skill):
    name = 'Walrus Punch'
    damage = 12
    stamina = 6

    def skill_effect(self) -> str:
        self.target.get_damage(self.damage)
        self.user.get_stamina_reduce(self.stamina)
        return f"""
        {os.linesep}{self.user.name} совершает свой коронный удар — настолько мощный, что подбрасывает жертву в воздух,
         нанося ей {self.damage} урона."""
