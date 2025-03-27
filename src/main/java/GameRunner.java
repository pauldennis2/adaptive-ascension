import lombok.extern.slf4j.Slf4j;

@Slf4j
public class GameRunner {

    public static void main(String[] args) {
        System.out.println("Hello");
        Hero me = new Hero(50);
        me.takeDamage(10);
        System.out.println(me);

        log.info("Adaptive Ascension Java Version started.");
        log.debug("Debug message example");
        log.warn("Warning message example");
        log.error("Error message example");
    }
}