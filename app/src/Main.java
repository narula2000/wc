import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        ArgumentParser parser = new ArgumentParser(args);
        parser.processFlags();
    }
}