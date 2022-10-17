from classes.abstract_skills import Skill


class FuryPunch(Skill):
    name = "Walrus Punch"
    damage = 350
    stamina = 100

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.health -= self.damage
        return f"""{self.user.name} совершает свой коронный удар — настолько мощный, что подбрасывает жертву в воздух,
         нанося ей критический урон."""


