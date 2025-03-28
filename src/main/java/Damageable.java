import lombok.AllArgsConstructor;

@AllArgsConstructor
public class Damageable {

    private int hp;

    public void takeDamage(int amount) {
        hp -= amount;
    }

    public boolean isDead() {
        return hp > 0;
    }
    //Could return boolean
}
