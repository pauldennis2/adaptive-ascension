import lombok.*;

@Getter
@Builder
@EqualsAndHashCode
public class Card {

    public static final Card BASIC_ATTACK = Card.builder().name("Basic Attack").damage(3).build();
    public static final Card BASIC_DEFEND = Card.builder().name("Basic Defend").block(3).build();
    public static final Card IRON_WAVE = Card.builder().name("Iron Wave").damage(3).block(3).build();
    public static final Card RECKLESS_ATTACK = Card.builder().name("Reckless Attack")
        .damage(7)
        .additionalEffect(hero -> hero.takeDamage(1)).build();

    @NonNull
    private String name;
    private int damage;
    private int block;

    private HeroAction additionalEffect;
    //boolean starter/basic
    //enum type (attack, skill, power)
}
