from classes.skills.abstract_skills import Skill


class FuryPunch(Skill):
    name = "Walrus Punch"
    damage = 12
    stamina = 6

    def skill_effect(self) -> str:
        self.user._stamina -= self.stamina
        self.target._hp -= self.damage
        return f"""{self.user.name} совершает свой коронный удар — настолько мощный, что подбрасывает жертву в воздух,
         нанося ей критический урон."""


