package count;
import java.util.*;

public class Lab_2_Ex_4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		
		System.out.println ("please enter the dimensions of the arrays to be added:\n");
		int m = sc.nextInt();
		int n = sc.nextInt();
		int a [][] = new int [m][n];
		int b [][] = new int [m][n];
		int c [][] = new int [m][n];
		System.out.println("pleas enter the 1st array:\n");
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				a [i][j]= sc.nextInt();
			}
		}
		System.out.println("pleas enter the 2nd array:\n");
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				b [i][j]= sc.nextInt();
			}
		}
		System.out.println("the added array is:\n");
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				c[i][j]=a[i][j]+b[i][j];
				System.out.print (c[i][j]+ "   ");}
			System.out.println();
		}
	}

}
