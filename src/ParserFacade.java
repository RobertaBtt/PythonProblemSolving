import java.io.*;
import java.util.Optional;

/**
 * This class is thread safe.
 */
public class ParserFacade {

    private static ParserFacade instance;

    public static ParserFacade getInstance() {
        if (instance == null) {
            instance = new ParserFacade();
        }
        return instance;
    }

    private File file;

    public synchronized void setFile(File f) {
        file = f;
    }

    public synchronized Optional<File> getFile() {
        if (file != null) {
            return Optional.of(file);
        } else {
            return null;
        }
    }

    public String getContent() throws IOException {
        FileInputStream i = new FileInputStream(file);
        String output = "";
        int data;
        while ((data = i.read()) > 0) output += (char) data;
        return output;
    }
    public String getContentWithoutUnicode() throws IOException {
        FileInputStream i = new FileInputStream(file);
        String output = "";
        int data;
        while ((data = i.read()) > 0) if (data < 0x80) {
            output += (char) data;
        }
        return output;
    }
    public void saveContent(String content) throws IOException {
        FileOutputStream o = new FileOutputStream(file);
        for (int i = 0; i < content.length(); i += 1) {
            o.write(content.charAt(i));
        }
    }
}