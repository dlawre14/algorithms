import classes.structures.containers.array.Stack;

/**
 * Created by Dylan on 4/17/2015.
 */
public class Driver {

    public static void main (String[] argv) {
        Stack<Integer> s = new Stack<Integer>();

        s.push(3);
        s.push(4);
        s.push(5);

        System.out.println("Current size: " + s.getSize() + " Current capacity: " + s.getCapacity());

        s.push(1);

        System.out.println("Current size: " + s.getSize() + " Current capacity: " + s.getCapacity());

        Integer i = s.pop();
        System.out.println(i);

        System.out.println("Current size: " + s.getSize() + " Current capacity: " + s.getCapacity());

        i = s.pop();
        System.out.println(i);
        i = s.pop();
        System.out.println(i);
        i = s.pop();
        System.out.println(i);
    }

}
