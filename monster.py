import math

class Monster:
    REGEN_ABILITY = lambda combat_state, monster: setattr(monster, "hp", monster.hp + 3)
    EXTRA_DAMAGE_ABILITY = lambda combat_state, monster: setattr(combat_state["hero_hp"], combat_state["hero_hp"] - 2)

    def __init__(self, floor: int):
        """
        Initializes a Monster instance.

        Args:
            floor: The floor number, used to scale monster stats.
        """
        self.floor = floor
        self.hp = self._calculate_hp()
        self.damage = self._calculate_damage()
        self.abilities = self._determine_abilities()

    def _calculate_hp(self) -> int:
        """Calculates monster HP based on floor (non-linear)."""
        return 10 + int(math.pow(self.floor, 1.5))

    def _calculate_damage(self) -> int:
        """Calculates monster damage based on floor (non-linear)."""
        return 2 + int(math.pow(self.floor // 2, 1.5))

    def _determine_abilities(self) -> list:
        """Determines monster abilities based on floor."""
        abilities = []
        if self.floor % 5 == 0:
            abilities.append(Monster.REGEN_ABILITY)
        if self.floor % 7 == 0:
            abilities.append(Monster.EXTRA_DAMAGE_ABILITY)
        return abilities

    def apply_abilities(self, combat_state: dict):
        """Applies monster abilities to the combat state."""
        for ability in self.abilities:
            ability(combat_state, self)  # Pass monster instance

    def take_damage(self, damage: int):
        """Reduces monster HP by the given damage."""
        self.hp = max(0, self.hp - damage)

    def is_dead(self) -> bool:
        """Returns True if the monster is dead, False otherwise."""
        return self.hp <= 0

    def __repr__(self) -> str:
        return f"Monster(Floor: {self.floor}, HP: {self.hp}, Damage: {self.damage}, Abilities: {len(self.abilities)})"