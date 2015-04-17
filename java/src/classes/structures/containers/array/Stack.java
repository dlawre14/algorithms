package classes.structures.containers.array;

import helpers.ArrayPrinter;

import java.util.EmptyStackException;

/**
 * Created by Dylan on 4/17/2015.
 *
 * This is an array based stack
 */

public class Stack<T> {

    private T[] array;
    private int size;
    private int capacity;

    public Stack() {
        array = (T[]) new Object[1];
        size = 0;
        capacity = 1;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }

    public void push(T element) {
        array[size] = element;
        size++;

        //If we have filled the stack, double our capacity
        if (size == capacity) {
            capacity *= 2;
            T[] temp = (T[]) new Object[capacity];
            for (int i = 0; i < size; i++)
                temp[i] = array[i];
            array = temp.clone();
        }
    }

    public T pop() {
        if (size < 1)
            throw new EmptyStackException();

        return array[--size];
    }
}
