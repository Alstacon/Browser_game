from dataclasses import dataclass

import marshmallow


@dataclass
class Weapon:
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    def caused_damage(self):
        pass

    class Meta:
        unknown = marshmallow.EXCLUDE
