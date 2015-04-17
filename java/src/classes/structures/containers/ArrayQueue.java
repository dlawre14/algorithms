package classes.structures.containers;

/**
 * Created by Dylan on 4/17/2015.
 */
public class ArrayQueue<T>  {

    private T[] array;
    private int size;

    public ArrayQueue() {
        size = 0;
        array = (T[]) new Object[1];
    }

    public void push(T element) {
        array[size] = element;
        size++;

        //Need to resize the array, Note: Choosing not to use utils for copying
        if (size == array.length) {
            T[] temp = (T[]) new Object[size*2];
            for (int i = 0; i < size; i++)
                temp[i] = array[i];
            array = (T[]) temp.clone();
        }
    }
}
