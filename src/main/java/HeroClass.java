import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
 public enum HeroClass {
    HEALER(50),
    TANK(75),
    SPEEDY(40);

    private final int startingHp;
}
