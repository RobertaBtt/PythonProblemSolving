package src;

import java.text.SimpleDateFormat;
import java.util.*;

public class TestCodility {

    private static HashMap<String, Integer> hashMapLog = new HashMap<String, Integer>();
    private static HashMap<String, Integer> hashMapLogPay = new HashMap<String, Integer>();
    private static String format = "hh:mm:ss";
    private static int phoneNumberPosition = 1;
    private static int callDurationPosition = 0;

    private static int maxSecondsForPromotion = 300;

    private static int secondsCents = 3;
    private static int minuteCents = 150;

    private static int totalToPay = 0;

    public static void main(String args[]) {

        solution(format);
        System.exit(0);
    }


    public static int solution(String format) {
        String s =
                "00:01:07,400-234-090\n" +
                        "00:05:01,701-080-080\n" +
                        "00:05:00,400-234-090";

        int tempDuration = 0;

        String[] logs = s.split("\n");

        for (String log : logs) {

            tempDuration = getDurationInSeconds(log.split(",")[callDurationPosition], format);
            updateHashMap(log.split(",")[phoneNumberPosition], tempDuration);
        }


        String valueToExclude = maxUsingCollectionsMax(hashMapLog);
        hashMapLogPay.remove(valueToExclude);

        for (float f : hashMapLogPay.values()) {
            totalToPay += f;
        }

        System.out.println(totalToPay);
        return totalToPay;
    }

    private static int getDurationInSeconds(String dataString, String dataPattern) {

        SimpleDateFormat sdf = new SimpleDateFormat(dataPattern);
        Date date;
        int seconds;
        int hours;
        int minutes;

        int durationTotal = 0;
        try {
            date = sdf.parse(dataString);
            seconds = date.getSeconds();
            minutes = date.getMinutes();
            hours = date.getHours();

            durationTotal = seconds + (minutes * 60) + (hours * 60 * 60);
        } catch (Exception ex) {
        }
        return durationTotal;

    }

    private static void updateHashMap(String phoneNumber, Integer durationInSeconds) {

        Integer updatedDuration;
        Integer updatedPayment;

        if (hashMapLog.containsKey(phoneNumber)) {
            updatedDuration = hashMapLog.get(phoneNumber) + durationInSeconds;

        } else {
            updatedDuration = durationInSeconds;
        }

        updatedPayment = getPayment(updatedDuration);
        hashMapLogPay.put(phoneNumber, updatedPayment);
        hashMapLog.put(phoneNumber, updatedDuration);

    }

    private static int getPayment(int updatedDuration){

        int updatedPayment;

        if (updatedDuration < maxSecondsForPromotion){
            updatedPayment = updatedDuration * secondsCents;
        }
        else{

            if ((updatedDuration % 60) == 0){
                updatedPayment = (updatedDuration / 60) * minuteCents;
            }
            else{
                updatedPayment = ((updatedDuration / 60)+1) * minuteCents;
            }
        }

        return updatedPayment;

    }

    public static <K, V extends Comparable<V>> String maxUsingCollectionsMax(Map<K, V> map) {
        Map.Entry<K, V> maxEntry = Collections.max(map.entrySet(), new Comparator<Map.Entry<K, V>>() {
            public int compare(Map.Entry<K, V> e1, Map.Entry<K, V> e2) {
                return e1.getValue()
                        .compareTo(e2.getValue());
            }
        });
        return (String) maxEntry.getKey();
    }


}