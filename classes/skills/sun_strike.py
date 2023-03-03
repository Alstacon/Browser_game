from classes.skills.abstract_skills import Skill


class SunStrike(Skill):
    name = 'Sun Strike'
    damage = 25
    stamina = 10

    def skill_effect(self) -> str:
        self.target.get_damage(self.damage)
        self.user.get_stamina_reduce(self.stamina)
        return f"""{self.user.name} посылает катастрофический луч ожесточённой энергии солнца, который
        наносит {self.damage} урона."""
