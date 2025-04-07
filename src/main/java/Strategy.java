import java.util.ArrayList;
import java.util.List;

public class Strategy {

    //As a strategy I need to know about my hero. Strategy might eventually contain Hero

    public static final HeroAction INCREASE_HP = (hero -> hero.addMaxHp(2));
    public static final HeroAction REMOVE_BASIC_ATTACK = (hero -> hero.removeCard(Card.BASIC_ATTACK));
    public static final HeroAction REMOVE_BASIC_DEFEND = (hero -> hero.removeCard(Card.BASIC_DEFEND));
    public static final HeroAction ADD_RECKLESS_ATTACK = (hero -> hero.addCard(Card.RECKLESS_ATTACK));
    public static final HeroAction ADD_IRON_WAVE = (hero -> hero.addCard(Card.IRON_WAVE));

    //Not sure yet where this is called, could be private
    List<HeroAction> getOptions() {
        List<HeroAction> options = new ArrayList<>();
        options.add(INCREASE_HP);
        options.add(ADD_RECKLESS_ATTACK);
        options.add(ADD_IRON_WAVE);

        if (hero.hasCard(Card.BASIC_ATTACK)) {
            options.add(REMOVE_BASIC_ATTACK);
        }
        if (hero.hasCard(Card.BASIC_DEFEND)) {
            options.add(REMOVE_BASIC_DEFEND);
        }
        return options;
    }

    private List<HeroAction> preferenceOrder;

    private Hero hero;
}
