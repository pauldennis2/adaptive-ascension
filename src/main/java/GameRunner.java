public class GameRunner {

    public static void main(String[] args) {
        System.out.println("Hello");
        Hero me = new Hero(50);
        me.takeDamage(10);
        System.out.println(me);
    }
}