import java.util.*;
//a. Write a method isPrime to accept one integer parameter and to check whether that parameter is prime or not
//b. Using this method, generate first N prime numbers in the main method.
public class Lab_1_Ex_4 {
	public static boolean isPrime(int num) {
		boolean flag = true;
		for (int i= 1; i<num/2 ;++i) {
			if (num%i == 0) flag = false;
		}
		return flag;
	}
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		int number = scan.nextInt();
		boolean ans = isPrime(number);
		if (ans == true) System.out.println("number is prime");
		else System.out.println("number is not prime");

		int N = scan.nextInt();
		count = 0;
		while(count <N){
			if (isPrime(num))
				System.out.print(num + " ");
		}
		scan.close();
	}

}
