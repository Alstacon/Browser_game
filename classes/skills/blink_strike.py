from classes.skills.abstract_skills import Skill


class BlinkStrike(Skill):
    name = "Blink Strike"
    damage = 15
    stamina = 5

    def skill_effect(self) -> str:
        self.user.stamina_points -= self.stamina
        self.target.health_points -= self.damage
        return f"""{self.user.name} телепортируется за спину врага и наносит ему урон."""


