from classes.skills.abstract_skills import Skill


class BlinkStrike(Skill):
    name = "Blink Strike"
    damage = 150
    stamina = 50

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.health -= self.damage
        return f"""{self.user.name} телепортируется за спину врага и наносит ему урон."""


