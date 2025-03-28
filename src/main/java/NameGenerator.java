import java.util.List;
import java.util.Random;

public class NameGenerator {

    //Playing around with making fun names
    public static final List<String> ADJECTIVES = List.of("Robust", "Merciful", "Lordly", "Fiery", "Tranquil", "Smelly");
    public static final List<String> COLORS = List.of("Red", "Cyan", "Indigo", "Pink", "Green", "Brown");
    public static final List<String> NOUNS = List.of("River", "Horse", "Turtle", "Ocean", "Mountain", "Tempest", "Cactus", "Slime");

    static Random random = new Random();

    public static String makeName() {
        return ADJECTIVES.get(random.nextInt(ADJECTIVES.size())) + "-"
                + COLORS.get(random.nextInt(COLORS.size())) + "-"
                + NOUNS.get(random.nextInt(NOUNS.size())) + "-"
                + random.nextInt(1_000, 10_000);
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.println(makeName());
        }
    }
}
