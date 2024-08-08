import java.util.*;
//a. Write a method reverse() to accept one integer parameter and to return the reversed digits of accepted number
//b. Using this method, check whether the inputted number is a palindrome or not.
public class Lab_1_Ex_2 {
	
	public static int reverse(int num) {
		int reversed =0;
		while (num != 0) {
			int digit = num % 10;
			reversed = reversed * 10 + digit;
			num /= 10;
		}
		return reversed;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		
		int number = a;
		a = reverse(a);
		
		if (number == a)
		System.out.println("The Number is a Palindrome");
		else
		System.out.println("The Number is not a Palindrome");
		
		scan.close();
	}

}
