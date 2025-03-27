class Card:
    def __init__(self, attack: int = 0, block: int = 0):
        """
        Initializes a Card instance.

        Args:
            attack: The attack value of the card.
            block: The block value of the card.
        """
        self.attack = attack
        self.block = block

    def __repr__(self) -> str:
        return f"Card(Attack: {self.attack}, Block: {self.block})"