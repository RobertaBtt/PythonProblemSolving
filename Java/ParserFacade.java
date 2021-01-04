package src;

import java.io.*;
import java.util.Optional;

/**
 * This class is thread safe.
 */
public class ParserFacade {

    private File file;
    private boolean checkDimension = true;
    private int maxDimension = 0x80;

    private static ParserFacade instance;
    private ParserFacade(){}

    public static ParserFacade getInstance() {
        if (instance == null) {
            instance = new ParserFacade();
        }
        return instance;
    }

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
        FileInputStream fileInputStream = null;
        String output = "";
        int data;

        try{
            fileInputStream = new FileInputStream(file);
        }
        catch (FileNotFoundException ex){}

        if (fileInputStream != null){
            while ((data = fileInputStream.read()) > 0){
                if (checkDimension){
                    /*Appending data only if data is  maxDimension*/
                    if (data < maxDimension){
                        output += (char) data;
                    }

                }
                else{
                    /*Appending data without checking maxDimension*/
                    output += (char) data;
                }

            }
        }


        return output;
    }


    public void saveContent(String content) throws IOException {

        FileOutputStream o = null;
        try{
            o = new FileOutputStream(file);
        }
        catch (FileNotFoundException ex){ }
        if (o != null){

            for (int i = 0; i < content.length(); i += 1) {
                o.write(content.charAt(i));
            }
        }


    }
}