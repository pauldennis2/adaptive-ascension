import lombok.Getter;
import lombok.NonNull;

import java.util.ArrayList;
import java.util.List;

@Getter
public class Hero extends Damageable{

    public static final int NUM_BASICS = 4;

    private int hp;
    private int maxHp;

    @NonNull
    private List<Card> deck;
    private Strategy strategy;

    public Hero(HeroClass heroClass) {
        super(heroClass.getStartingHp());
        this.maxHp = heroClass.getStartingHp();
        deck = new ArrayList<>();
        for (int i = 0; i < NUM_BASICS; i++) {
            deck.add(Card.BASIC_ATTACK);
            deck.add(Card.BASIC_DEFEND);
        }
    }

    public String toString() {
        return "HP: " + hp;
    }

    //No protection on negative at this time
    public void addMaxHp(int amount) {
        hp += amount;
        maxHp += amount;
    }

    public void addCard(Card card) {
        deck.add(card);
        //TODO add at start of list?
    }

    public void removeCard(Card card) {
        deck.remove(card);
    }

    public boolean hasCard(Card card) {
        return deck.contains(card);
    }
}
