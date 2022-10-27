from classes.units.abstract_unit import BaseUnit


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        if self.stamina_points < 5:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        else:
            damage = self._count_damage(target)
            if damage != 0:
                return f"""{self.name} используя {self.weapon.name}
                пробивает {target.armor.name} соперника и наносит {damage} урона."""
            else:
                return f"""{self.name}, используя {self.weapon.name} наносит удар, но {target.armor.name}
                cоперника его останавливает."""
