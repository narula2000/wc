package FlagHandler;

public class CFlagHandler implements FlagHandler {
    @Override
    public void handle(String value, boolean isPipedInput) {
        System.out.println("Handling -c flag with value: " + value);
    }
}
