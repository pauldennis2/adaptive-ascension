import logging
import itertools
from typing import List, Dict, Callable
from hero import Hero
from monster import Monster

# Assuming Card, Hero, and Monster classes are defined in their respective files

def perform_combat(hero: Hero, monster: Monster, log_combat: bool = False) -> bool:
    """Simulates a combat encounter."""
    hero_block = 0
    combat_state = {"hero": hero}

    if log_combat:
        logging.basicConfig(level=logging.INFO)

    while not hero.is_dead() and not monster.is_dead():
        hero_block = 0
        card_draw_count = 3 if hero.hero_class == "Speedy" else 2
        played_cards = hero.deck[:card_draw_count]
        hero.deck = hero.deck[card_draw_count:] + played_cards

        if log_combat:
            logging.info(f"Hero plays: {played_cards}")

        for card in played_cards:
            monster.take_damage(card.attack)
            hero_block += card.block
            hero.take_damage(card.self_damage)

        if log_combat:
            logging.info(f"Monster HP: {monster.hp}, Hero Block: {hero_block}, Hero HP: {hero.hp}")

        if monster.is_dead():
            hero.apply_class_ability()
            return True

        monster.apply_abilities(combat_state)
        attack_damage = max(0, monster.damage - hero_block)
        hero.take_damage(attack_damage)

        combat_state["hero"] = hero

        if log_combat:
            logging.info(f"Monster attacks for: {attack_damage}, Hero HP: {hero.hp}")

    if log_combat:
        logging.info("Monster wins!")
    return False

def main():
    classes = ["Healer", "Speedy", "Tank"] # removed None
    options = ["Remove Basic Attack", "Remove Basic Defend", "Increase Max HP (+2)", "Add Iron Wave", "Add Aggressive Attack"]
    strategies = list(itertools.permutations(options))

    results = []

    for hero_class in classes:
        for strategy in strategies:
            hero = Hero(hero_class=hero_class)
            hero.strategy.preferences = list(strategy)
            floor = 1

            while True:
                monster = Monster(floor)
                if perform_combat(hero, monster, log_combat=True):
                    improvement_option = hero.strategy.choose_option(hero.get_improvement_options())
                    if improvement_option:
                        improvement_option()
                    floor += 1
                else:
                    results.append((floor, hero.strategy, hero_class))
                    print(f"Hero with Strategy {hero.strategy} and Class {hero_class} perished on Floor {floor}")
                    break

    results.sort(key=lambda x: x[0])  # Sort by floor reached

    print("\nTop 5:")
    for floor, strategy, hero_class in results[-5:]:
        print(f"Floor {floor}, Strategy {strategy}, Class {hero_class}")

    print("\nBottom 5:")
    for floor, strategy, hero_class in results[:5]:
        print(f"Floor {floor}, Strategy {strategy}, Class {hero_class}")

if __name__ == "__main__":
    main()