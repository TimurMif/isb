import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String PATH_TO_FILE = "java_sequence.txt";
        String sequence = generateRandomSequence();

        System.out.println(sequence);
        try {
            writeInFile(PATH_TO_FILE ,sequence);
        } catch (Exception e) {
            System.out.println("Error:" + e.getMessage());
        }
    }

    /**
     * A function that generates a random binary sequence
     *
     * @return The Binary sequence
     */
    public static String generateRandomSequence() {
        String sequence = "";
        for (int i = 0; i < 128; i++) {
            int randomValue = 1 + (int) (Math.random() * 2);
            if (randomValue == 1) {
                sequence += "1";
            } else {
                sequence += "0";
            }
        }
        return sequence;
    }

    /**
     * A function for writing content to a file
     *
     * @param path File path
     * @param content The content that we write to the file
     *
     */
    public static void writeInFile(String path, String content) {
        try {
            File file = new File(path);
            file.createNewFile();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        try {
            FileWriter writer = new FileWriter(path);
            writer.write(content);
            writer.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}