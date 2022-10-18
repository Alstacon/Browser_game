from classes.units.abstract_unit import BaseUnit


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        if self.stamina < 20:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        else:
            if damage := self._count_damage(target) != 0:
                return f"""{self.name} используя {self.weapon.name}
                пробивает {target.armor.name} соперника и наносит {damage} урона."""
            else:
                f"""{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name}
                cоперника его останавливает."""
