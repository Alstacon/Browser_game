from classes.arena.base_arena import BaseSingleton
from classes.units.abstract_unit import BaseUnit
from classes.units.enemy_unit import EnemyUnit
from classes.units.player_unit import PlayerUnit


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 20
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
            self.battle_result = "Не могу поверить, Вы проиграли!"
        if self.enemy.health_points <= 0:
            self.battle_result = "Битва отгремела не напрасно! Вы победили!"
        if self.player.health_points <= 0 and self.enemy.health_points <= 0:
            self.battle_result = "Никто не устоял в бою! Ничья!"
        return self.battle_result

    def _stamina_regeneration(self) -> None:
        self.player._stamina += self.STAMINA_PER_ROUND
        if self.player._stamina > self.player.unit_class.max_stamina:
            self.player._stamina = self.player.unit_class.max_stamina

        self.enemy._stamina += self.STAMINA_PER_ROUND
        if self.enemy._stamina > self.enemy.unit_class.max_stamina:
            self.enemy._stamina = self.enemy.unit_class.max_stamina

    def next_turn(self) -> str:
        if result := self._check_players_hp():
            return result
        self._stamina_regeneration()
        return self.enemy.hit(self.player)

    def end_game(self) -> str:
        result = self._check_players_hp()
        self._instances = {}
        self.game_is_running = False
        return result

    def player_hit(self) -> str:
        result = self.player.hit(self.enemy)
        return result

    def player_use_skill(self) -> str:
        result = self.player.use_skill(self.enemy)
        self.next_turn()
        return result


