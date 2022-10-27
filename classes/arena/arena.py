from classes.arena.base_arena import BaseSingleton
from classes.units.abstract_unit import BaseUnit


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self) -> str | None:
        if self.player.health_points <= 0:
            return "Не могу поверить, Вы проиграли!"
        if self.enemy.health_points <= 0:
            return "Битва отгремела не напрасно! Вы победили!"
        if self.player.health_points <= 0 and self.enemy.health_points <= 0:
            return "Никто не устоял в бою! Ничья!"

    def _stamina_regeneration(self) -> None:
        self.player._stamina = round(
            self.player._stamina + self.STAMINA_PER_ROUND * self.player.unit_class.stamina, 2
        )
        if self.player._stamina > self.player.unit_class.max_stamina:
            self.player._stamina = self.player.unit_class.max_stamina

        self.enemy._stamina = round(
            self.enemy._stamina + self.STAMINA_PER_ROUND * self.enemy.unit_class.stamina, 2
        )
        if self.enemy._stamina > self.enemy.unit_class.max_stamina:
            self.enemy._stamina = self.enemy.unit_class.max_stamina

    def next_turn(self) -> str | list:
        if self._check_players_hp():
            return self.end_game()
        else:
            self._stamina_regeneration()
            return self.enemy.hit(self.player)

    def end_game(self) -> str:
        result = self._check_players_hp()
        self._instances = {}
        self.game_is_running = False
        return result

    def player_hit(self) -> list:
        result = [self.player.hit(self.enemy), self.next_turn()]
        return result

    def player_use_skill(self) -> list:
        result = [self.player.use_skill(self.enemy), self.next_turn()]
        return result
