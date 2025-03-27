import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class HeroTest {

    @Test
    void takeDamage() {
        Hero hero = new Hero(100);
        hero.takeDamage(20);
        assertEquals(80, hero.getHp());
    }
}