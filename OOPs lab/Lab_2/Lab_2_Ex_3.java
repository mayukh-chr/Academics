package count;
import java.util.*;

public class Lab_2_Ex_3 {
	
	boolean isPrime(int n) {
		boolean flag = true;
		for (int i=2; i<=n/2; i++) {
			if (n%i == 0) {
				flag = false;
			}
		}
		return flag;
	}

	public static void main(String[] args) {
		Lab_2_Ex_3 l = new Lab_2_Ex_3();
		Scanner scan = new Scanner (System.in);
		System.out.println("Enter size of array \n");
		int n = scan.nextInt();
		int arr[] = new int [n];
		System.out.println("Enter the elements \n");
		
		for (int i =0; i<arr.length; i++)
			arr[i] = scan.nextInt();
		
		for (int i =0; i<arr.length ; i++) {
			if (l.isPrime(arr[i]) == true)
			System.out.println(arr[i]);
		}
		
		scan.close();
		
		
			}
		}


