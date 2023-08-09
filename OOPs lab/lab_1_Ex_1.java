
import java.util.*;
//Create a method max() that has three integer parameters x,y,z and it returns the largest of the three. Do it two ways: once using an if-else-if ladder and once using nested if statements.
public class lab_1 {
	
	public static int maxnested(int x, int y, int z) {
		if (x>y) {
			if (z>x)return z;
			else return x;
		}
		else {
			if (x>y) return x;
			else return y;
		}
	}

	public static int maxifelse(int x, int y, int z) {
		
		if (x>y && x>z) return x;
		else if (y>z && y>x) return y;
		else return z;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		int a = scan.nextInt();
		int b = scan.nextInt();
		int c = scan.nextInt();
		
		int maxnest = maxnested(a,b,c);
		int maxif = maxifelse(a,b,c);
		
		System.out.println("Using nested if else: " + maxnest);
		System.out.println("Using if-else-if: " + maxif);
		scan.close();
	}

}
