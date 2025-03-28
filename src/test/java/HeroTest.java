import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class HeroTest {

    @Test
    void takeDamage() {
        Hero hero = new Hero(HeroClass.TANK);
        hero.takeDamage(20);
        assertEquals(55, hero.getHp());
    }
}