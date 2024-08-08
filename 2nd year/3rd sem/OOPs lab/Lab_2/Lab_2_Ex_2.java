package count;
import java.util.*;

public class Lab_2_Ex_2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner (System.in);
		System.out.println("Enter size of array");
		int n = scan.nextInt();
		
		int[] arr = new int[n];
		
		for (int i = 0; i<n;i++)
			arr[i] = i+1;
		
		for (int i: arr)
			System.out.print(i + " ");

		scan.close();
	}

}
