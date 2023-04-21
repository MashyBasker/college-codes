class A {
    public static void execute(String[] args) {
        if(true) {
            // break can only be used in a loop
            // if we just want to exit. leaving the if statement
            // empty is the best option
        }
    }
}

class Demo {
    public static void execute(String[] arr) {
        Integer num1 = 100;
        Integer num2 = 100;
        Integer num3 = 500;
        Integer num4 = 500;

        if(num1 == num2) {
            System.out.println("num1 == num2");
        }
        else {
            System.out.println("num3 != num4");
        }

        if(num3 == num4) {
            System.out.println("num3 == num4");
        } 
        else {
            System.out.println("num3 != num4");
        }
    }
}

interface I1 {
    String toString();
}

class Example {
    public static void execute(String args[]) {
        System.out.println(new I1() {
            public String toString() {
                System.out.print("Example");
                return ("A");
            }
        });
    }
}

class Test1 {
    // if the static keyword is removed
    // the variable cannot be accessed in the static context and hence will lead to compilation
    // error
    static int x = 10;
    public
    static void execute(String[] args) {
        System.out.println(x);
    }
    static {
        System.out.print(x + " ");
    }
}

class Test implements Runnable {
    public void run() {System.out.printf("%d", 3);}
    public static void execute(String[] args)
    throws InterruptedException {
        Thread thread = new Thread(new Test());
        thread.start();
        System.out.printf("%d", 1);
        thread.join();
        System.out.printf("%d", 2);
    }
}

public class prog {
    public static void main(String[] args) {
        System.out.println("\nClass A is executed");
        A.execute(args);
        System.out.println("\nClass Demo is executed");
        Demo.execute(args);
        System.out.println("\nClass Example is executed");
        Example.execute(args);
        System.out.println("\nClass Test1 is executed");
        Test1.execute(args);
        System.out.println("\nClass Test is executed");
        try {
            Test.execute(args);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

// to keep all the classes in the same file, the main functions of each class has been changed to "execute"
// otherwise the JRE will not know which main method to choose as an entry point