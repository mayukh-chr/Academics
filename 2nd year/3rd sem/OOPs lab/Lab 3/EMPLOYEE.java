package count;

import java.util.Scanner;

//import java.util.*;

public class EMPLOYEE {
	String name;
	int Eid;
	double basic;
	double DA;
	double gross_sal;
	double net_sal;
	
	void read() {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter Employee name: ");
		name = scan.next();
		System.out.println("Enter employee ID");
		Eid = scan.nextInt();
		System.out.println("Enter Basic Salary");
		basic = scan.nextDouble();
		scan.close();
	}
	
	void compute_net_sal() {
		DA = 0.52*basic;
		gross_sal = basic + DA;
		double IT = 0.30* gross_sal;
		net_sal = gross_sal -IT;
	}
	
	void display() {
		System.out.println("Employee name: " + name);
		System.out.println("Employee ID: " + Eid);
		System.out.println("Basic Salary: " + basic);
		System.out.println("DA: " + DA);
		System.out.println("gross salary: " + gross_sal);
		System.out.println("net salary: " + net_sal);
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("no. of employees");
		int N = scan.nextInt();
		
		EMPLOYEE[] employees = new EMPLOYEE[N];
		
		for(int i =0; i<N; i++)
		{
			employees[i] = new EMPLOYEE();
			System.out.println("\n Enter details for employee " + (i+1) + ":");
			employees[i].read();
			employees[i].compute_net_sal();
		}
		
		System.out.println("\n employee details: ");
		
		for(int i =0; i<N; i++) {
		System.out.println("\n details for employee " + (i+1) + ":");
		employees[i].display();
		}
		scan.close();
	}
	

}
