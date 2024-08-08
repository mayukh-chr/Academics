package count;
import java.util.*;

public class STUDENT {
	String sname;
	int[] marksArray = new int [4];
	int total;
	double average;
	
	void assign(String sname, int[] marksArray) {
		this.sname =sname;
		this.marksArray = marksArray;
	}
	
	void compute() {
		total =0;
		for (int mark : marksArray)
			total += mark;
		average = (double) total/marksArray.length;
	}
	
	void display() {
		System.out.println("Student Name: " + sname);
		System.out.println("marks: " + Arrays.toString(marksArray));
		System.out.println("Total marks: " + total);
		System.out.println("Average marks: " + average);
	}
	
	public static void main(String[] args) {
		STUDENT student1 = new STUDENT();
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter name: ");
		String name = scan.next();
		System.out.print("Enter marks: ");
		
		
		for(int j=0;j<4;j++) {
			student1.marksArray[j] = scan.nextInt();
		}
		student1.assign(name, student1.marksArray);
		student1.compute();
		student1.display();
		scan.close();
	}
	
}
