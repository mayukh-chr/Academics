public class Lab_4_Ex_2 {
    
    private static int objectCount = 0;

    
    public Lab_4_Ex_2() {
        
        objectCount++;
    }

    
    public static void showCount() {
        System.out.println("Number of Counter objects created: " + objectCount);
    }

    public static void main(String[] args) {
        
    	Lab_4_Ex_2 counter1 = new Lab_4_Ex_2();
    	Lab_4_Ex_2 counter2 = new Lab_4_Ex_2();
    	Lab_4_Ex_2 counter3 = new Lab_4_Ex_2();

        
    	Lab_4_Ex_2.showCount();
    }
}
