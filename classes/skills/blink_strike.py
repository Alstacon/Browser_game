import os

from classes.skills.abstract_skills import Skill


class BlinkStrike(Skill):
    name = 'Blink Strike'
    damage = 15
    stamina = 5

    def skill_effect(self) -> str:
        self.target.get_damage(self.damage)
        self.user.get_stamina_reduce(self.stamina)
        return f"""{os.linesep}{self.user.name} телепортируется за спину врага и наносит ему {self.damage} урона."""
