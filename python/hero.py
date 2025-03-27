from card import Card
from strategy import Strategy
from typing import List, Callable, Dict
from collections import defaultdict

class Hero:

    NUM_BASIC_ATTACKS = 4
    NUM_BASIC_DEFENDS = 4

    def __init__(self, max_hp: int = 50, hero_class: str = None):
        """
        Initializes a Hero instance with a starting deck, random strategy, and optional class.

        Args:
            max_hp: The maximum HP of the hero.
            hero_class: The hero's class ("Healer", "Speedy", "Tank").
        """
        self.max_hp = max_hp
        self.hp = max_hp
        self.deck: List[Card] = self._create_starting_deck()
        self.strategy = self._create_random_strategy()
        self.hero_class = hero_class

        if self.hero_class == "Speedy":
            self.max_hp -= 10
            self.hp -= 10
        if self.hero_class == "Tank":
            self.max_hp += 25
            self.hp += 25
    
    def _create_random_strategy(self) -> Strategy:
        """Creates a random strategy for the hero."""
        options = self.get_improvement_options()
        return Strategy(options)

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
        deck = []
        for i in range(max(self.NUM_BASIC_ATTACKS, self.NUM_BASIC_DEFENDS)):
            if i < self.NUM_BASIC_ATTACKS:
                deck.append(basic_attack)
            if i < self.NUM_BASIC_DEFENDS:
                deck.append(basic_defend)
        return deck
    
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
    
    def apply_class_ability(self):
        """Applies the hero's class ability."""
        if self.hero_class == "Healer":
            self.hp = min(self.max_hp, self.hp + 4)

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
    
    def print_deck(self):
        """Prints the hero's deck in the specified format."""
        card_counts = defaultdict(int)
        for card in self.deck:
            card_counts[card.name] += 1

        for card_name, count in card_counts.items():
            print(f"{card_name} x {count}")