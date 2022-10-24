from random import randint

from classes.units.abstract_unit import BaseUnit


class EnemyUnit(BaseUnit):
    is_skill_used = False

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар соперника
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target
        """
        chance = randint(0, 1)
        if chance == 1 and self.is_skill_used is False:
            self.is_skill_used = True
            return self.use_skill(target)
        else:
            if self.stamina_points < 5:
                return f"""{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."""
            else:
                damage = self._count_damage(target)
                if damage != 0:
                    return f"""{self.name} используя {self.weapon.name}
                           пробивает {target.armor.name} и наносит Вам {damage} урона."""
                else:
                    return f"""{self.name}, используя {self.weapon.name} наносит удар, но Ваш {target.armor.name}
                        его останавливает."""
