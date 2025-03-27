from typing import List, Callable, Dict

class Card:
    def __init__(self, attack: int = 0, block: int = 0, name: str = "Basic Card", self_damage: int = 0):
        """
        Initializes a Card instance.

        Args:
            attack: The attack value of the card.
            block: The block value of the card.
            name: The name of the card.
            self_damage: Damage dealt to the hero when the card is played.
        """
        self.attack = attack
        self.block = block
        self.name = name
        self.self_damage = self_damage

    def __repr__(self) -> str:
        return f"Card(Name: {self.name}, Attack: {self.attack}, Block: {self.block}, Self Damage: {self.self_damage})"

    @staticmethod
    def available_cards() -> List["Card"]:
        """Returns a list of available cards for purchase."""
        return [
            Card(attack=7, name="Aggressive Attack", self_damage=1),
            Card(attack=3, block=3, name="Iron Wave"),
        ]