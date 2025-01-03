import FlagHandler.FlagHandler;
import FlagHandler.CFlagHandler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class ArgumentParser {
    private final Map<String, FlagHandler> handlers = new HashMap<>();
    private final Map<String, String> arguments = new HashMap<>();
    private String pipedInput = null;

    private void registerHandlers() {
        handlers.put("-c", new CFlagHandler());
    }

    private void parseArgs(String[] args) {
        for (int i = 0; i < args.length; i++) {
            String arg = args[i];
            if (arg.startsWith("-")) {
                if (i + 1 < args.length && !args[i + 1].startsWith("-")) {
                    arguments.put(arg, args[i + 1]);
                    i++;
                } else {
                    arguments.put(arg, null);
                }
            }
        }
    }

    private void readPipedInput() throws IOException {
        if (System.in.available() > 0) {
            StringBuilder input = new StringBuilder();
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String line;
            while ((line = reader.readLine()) != null) {
                input.append(line).append("\n");
            }
            pipedInput = input.toString().trim();
        }
    }

    private String readFile(String filePath) throws IOException {
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
        }
        return content.toString().trim();
    }

    public void processFlags() throws IOException {
        for (Map.Entry<String, String> entry : arguments.entrySet()) {
            String flag = entry.getKey();
            String filePath = entry.getValue();
            FlagHandler handler = handlers.get(flag);

            if (handler != null) {
                if (pipedInput != null) {
                    handler.handle(pipedInput, true); // Use piped input
                } else if (filePath != null) {
                    String fileContent = readFile(filePath);
                    handler.handle(fileContent, false); // Use file content
                } else {
                    System.out.println("Error: Flag " + flag + " requires a file path.");
                }
            } else {
                System.out.println("Unknown flag: " + flag);
            }
        }
    }

    public ArgumentParser(String[] args) throws IOException {
        registerHandlers();
        parseArgs(args);
        readPipedInput();
    }
}
