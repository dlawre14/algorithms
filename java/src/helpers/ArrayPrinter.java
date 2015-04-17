package helpers;

/**
 * Created by Dylan on 4/17/2015.
 */
public class ArrayPrinter {

    public static <T> void printArray(T[] array) {
        String out = "[";
        for (T element : array)
            out += element + ", ";
        out = out.substring(0, out.length()-2) + "]";

        System.out.println(out);
    }

}
