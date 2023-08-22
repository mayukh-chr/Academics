package count;
import java.util.*;

public class Lab_2_Ex_6 {
	public static void main (String [] args) {
		Scanner sc = new Scanner (System.in);
		int n = sc.nextInt();
		int a []= new int [n];
		for (int i=0; i<a.length; i++) {
			a[i]=sc.nextInt();
		}
		System.out.println("enter the element to be searched: ");
		int b = sc.nextInt();
		int f = 0;
		for (int i =0; i<a.length; i++) {
			if (a[i]==b) {
				f=1; break;
			}
		}
		if (f==1) {
			System.out.println ("element found!");
		}
		else 
			System.out.println ("element not found!"); 
			
	}

}
