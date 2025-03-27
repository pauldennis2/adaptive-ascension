import lombok.Getter;

public class Hero {

    @Getter
    private int hp;

    public Hero(int hp) {
        this.hp = hp;
    }

    public void takeDamage(int amount) {
        hp -= amount;
    }

    public String toString() {
        return "HP: " + hp;
    }
}
