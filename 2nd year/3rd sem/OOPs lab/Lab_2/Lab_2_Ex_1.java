package count;
import java.util.*;

public class Lab_2_Ex_1 {

	public static void main(String[] args) {
		//WAP that creates an array of integers and then uses a loop to reverse the order of the elements in the array
		Scanner scan = new Scanner (System.in);
		System.out.println("Enter size of the array");
		
		int n =  scan.nextInt();
		int arr[] = new int [n];
		
		System.out.println("Enter elements: ");
		
		for (int i=0;i<n;i++)
			arr[i] = scan.nextInt();
		
		for(int i=0; i<(n/2);i++) {
			int temp = arr[i];
			arr[i] = arr[n-i-1];
			arr[n-i-1] = temp;
		}
		for (int i=0;i<n;i++)
			System.out.print(arr[i] + " ");
		scan.close();
	}

}
