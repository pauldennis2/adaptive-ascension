import logging
from typing import List, Dict, Callable
from hero import Hero
from monster import Monster

# Assuming Card, Hero, and Monster classes are defined in their respective files

def perform_combat(hero: Hero, monster: Monster, log_combat: bool = False) -> bool:
    """Simulates a combat encounter."""
    hero_block = 0
    combat_state = {"hero": hero} # combat state now holds the hero object.

    if log_combat:
        logging.basicConfig(level=logging.INFO)

    while not hero.is_dead() and not monster.is_dead():
        hero_block = 0
        played_cards = hero.deck[:2]
        hero.deck = hero.deck[2:] + played_cards

        if log_combat:
            logging.info(f"Hero plays: {played_cards}")

        for card in played_cards:
            monster.take_damage(card.attack)
            hero_block += card.block
            hero.take_damage(card.self_damage)

        if log_combat:
            logging.info(f"Monster HP: {monster.hp}, Hero Block: {hero_block}, Hero HP: {hero.hp}")

        if monster.is_dead():
            return True

        monster.apply_abilities(combat_state)
        attack_damage = max(0, monster.damage - hero_block)
        hero.take_damage(attack_damage)

        if log_combat:
            logging.info(f"Monster attacks for: {attack_damage}, Hero HP: {hero.hp}")

    if log_combat:
        logging.info("Monster wins!")
    return False

def main():
    num_heroes = 10
    heroes = [Hero() for _ in range(num_heroes)]  # Create 10 heroes

    for hero_index, hero in enumerate(heroes):
        floor = 1
        while True:
            monster = Monster(floor)
            if perform_combat(hero, monster):
                # Hero wins
                improvement_option = hero.strategy.choose_option(hero.get_improvement_options())
                if improvement_option:
                    improvement_option()
                floor += 1
            else:
                # Hero loses
                print(f"Hero {hero_index + 1} with Strategy {hero.strategy} perished on Floor {floor}")
                break

if __name__ == "__main__":
    main()