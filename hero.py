from card import Card
from strategy import Strategy
from typing import List, Callable, Dict

class Hero:
    def __init__(self, max_hp: int = 50, deck: list[Card] = None):
        """
        Initializes a Hero instance.

        Args:
            max_hp: The maximum HP of the hero.
            deck: The hero's deck of cards.
        """
        self.max_hp = max_hp
        self.hp = max_hp
        self.deck: List[Card] = self._create_starting_deck()
        self.strategy = Strategy(self.get_improvement_options())

    def get_improvement_options(self) -> Dict[str, Callable[[], None]]:
        """
        Returns a dictionary of improvement options after combat.

        Returns:
            A dictionary where keys are option descriptions and values are callable functions.
        """
        options = {}

        if any(card.name == "Basic Attack" for card in self.deck):
            options["Remove Basic Attack"] = self._remove_basic_attack

        if any(card.name == "Basic Defend" for card in self.deck):
            options["Remove Basic Defend"] = self._remove_basic_defend

        options["Increase Max HP (+2)"] = self._increase_max_hp

        for card in Card.available_cards():
            options[f"Add {card.name}"] = lambda c=card: self.add_card(c)

        return options

    def _remove_basic_attack(self):
        """Removes a Basic Attack card from the deck."""
        for i, card in enumerate(self.deck):
            if card.name == "Basic Attack":
                del self.deck[i]
                break

    def _remove_basic_defend(self):
        """Removes a Basic Defend card from the deck."""
        for i, card in enumerate(self.deck):
            if card.name == "Basic Defend":
                del self.deck[i]
                break

    def _increase_max_hp(self):
        """Increases the hero's maximum HP by 2."""
        self.max_hp += 2
        self.hp += 2  # Heal the hero for the increase

    def _create_starting_deck(self) -> List[Card]:
        """Creates the hero's starting deck."""
        basic_attack = Card(attack=3, name="Basic Attack")
        basic_defend = Card(block=3, name="Basic Defend")
        return [basic_attack] * 5 + [basic_defend] * 5

    def take_damage(self, damage: int):
        """Reduces hero HP by the given damage."""
        self.hp = max(0, self.hp - damage)

    def is_dead(self) -> bool:
        """Returns True if the hero is dead, False otherwise."""
        return self.hp <= 0

    def add_card(self, card: Card):
        """Adds a card to the hero's deck."""
        self.deck.append(card)

    def __repr__(self) -> str:
        return f"Hero(HP: {self.hp}/{self.max_hp}, Deck: {len(self.deck)} cards)"