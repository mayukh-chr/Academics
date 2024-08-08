import java.util.Scanner;
//Write a method fact to accept one integer parameter and to find the factorial of a given number
// using fact method, computer (nCr) in the main method.
public class Lab_1_Ex_3 {

	public static int fact(int num) {
		int ans = 1;
		
		while (num >0 ) {
			ans *= num;
			num--;
		}
		return ans;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		int r = scan.nextInt();
		
		double factorial = (fact(num)/fact(num-r));
		
		System.out.println("C(" + num +"," + r + ")" + factorial);
		scan.close();
	}

}
