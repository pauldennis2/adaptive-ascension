from card import Card


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
        self.deck = deck if deck else []

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