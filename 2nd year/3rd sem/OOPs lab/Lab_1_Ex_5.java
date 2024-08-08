import java.util.*;
//Write a method findsum to find the sum of digits of a number.
public class Lab_1_Ex_5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		System.out.println("please enter n: ");
		int n = scan.nextInt();
		int x = n;
		int i= 0;
		while (x!=0) {
			i = i+x%10;
			x = x/10;
		}
		System.out.println("sum of digits of "+ n + " is: "+ i);
	
	}

}
