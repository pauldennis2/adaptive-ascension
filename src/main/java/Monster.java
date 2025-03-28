import lombok.Getter;

@Getter
public class Monster extends Damageable{

    private int damage;
    //possibly later move to a List<Attack> where attack has number and damage
    //List<MonsterAbility>... may need to expand HeroAction into "CombatAction"

    public Monster(int floor) {
        super((int)(10 + Math.pow(floor, 1.5)));
        this.damage = (int)(2 + Math.pow(floor, 1.2));
    }
}
