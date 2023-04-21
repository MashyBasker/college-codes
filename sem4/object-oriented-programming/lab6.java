public class lab6 {

    public static void executeA(String[] args) {
        if (true) {
            // If we just want to exit, leaving the if statement empty is the best option
        }
    }

    public static void executeDemo(String[] args) {
        Integer num1 = 100;
        Integer num2 = 100;
        Integer num3 = 500;
        Integer num4 = 500;

        if (num1 == num2) {
            System.out.println("num1 == num2");
        } else {
            System.out.println("num1 != num2");
        }

        if (num3 == num4) {
            System.out.println("num3 == num4");
        } else {
            System.out.println("num3 != num4");
        }
    }

    public static void executeExample(String[] args) {
        System.out.println(new I1() {
            public String toString() {
                System.out.print("Example");
                return ("A");
            }
        });
    }

    static class Test1 {
        static int x = 10;

        static {
            System.out.print(x + " ");
        }

        public static void execute(String[] args) {
            System.out.println(x);
        }
    }

    static class Test implements Runnable {
        public void run() {
            System.out.printf("%d", 3);
        }

        public static void execute(String[] args) throws InterruptedException {
            Thread thread = new Thread(new Test());
            thread.start();
            System.out.printf("%d", 1);
            thread.join();
            System.out.printf("%d", 2);
        }
    }

    interface I1 {
        String toString();
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("\nExecuting A");
        executeA(args);

        System.out.println("\nExecuting Demo");
        executeDemo(args);

        System.out.println("\nExecuting Example");
        executeExample(args);

        System.out.println("\nExecuting Test1");
        Test1.execute(args);

        System.out.println("\nExecuting Test");
        Test.execute(args);
    }
}
