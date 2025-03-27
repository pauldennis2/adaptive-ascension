import random
from typing import List, Callable, Dict

class Strategy:
    def __init__(self, options: Dict[str, Callable[[], None]]):
        """
        Initializes a Strategy instance with a random order of preferences.

        Args:
            options: A dictionary of available improvement options.
        """
        self.preferences = list(options.keys())
        random.shuffle(self.preferences)

    def choose_option(self, options: Dict[str, Callable[[], None]]) -> Callable[[], None]:
        """
        Chooses the best available option based on preferences.

        Args:
            options: A dictionary of available improvement options.

        Returns:
            The callable function representing the chosen option.
        """
        for option in self.preferences:
            if option in options:
                return options[option]
        return None  # No valid option found

    def __repr__(self) -> str:
        return f"Strategy(Preferences: {self.preferences})"