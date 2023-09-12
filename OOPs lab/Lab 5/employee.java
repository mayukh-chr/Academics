package aryannayaklab5;

import java.util.Scanner;

public class employee {
	
		double DAa,Gross_sall;
		String Enamee;
		int Eidd;
		String Ename;
		int Eid;
		double DA,Gross_sal,Net_Sal;
		employee(String Ename,int Eid,double DA,double Gross_sal)
		{
			this.Ename=Ename;
			this.Eid=Eid;
			this.DA=DA;
			this.Gross_sal=Gross_sal;
		}
		
		public static void Read(int n)
		{  
	     Scanner sc=new Scanner(System.in);
		 double DAa,Gross_sall;
		 String Enamee;
		 int Eidd;
		 employee[] time = new employee[n];
		 for(int i=0;i<n;i++)
		 {
			
			System.out.println("enter your name");
			String Enamee1=sc.nextLine();
			System.out.println("enetr your id");
			Eidd=sc.nextInt();
			System.out.println("Enter DA : ");
			DAa=sc.nextDouble();
			System.out.println("Enter Gross Salary : ");
			Gross_sall=sc.nextDouble();
			time[i]= new employee(Enamee1,Eidd,DAa,Gross_sall);
			time[i].compute_net_sal(time[i]);
			time[i].display(time[i]);
		}
		 sc.close();
		}
		public void compute_net_sal(employee ob)
		{
			ob.Net_Sal=ob.Gross_sal+ob.Gross_sal*0.52-ob.Gross_sal*0.3;
		}
		public void display(employee obj2)
		{
			System.out.println("Net salary is : "+obj2.Net_Sal);
		}
		public void formatEmployeename(employee ob)
		{
			char temp;
			String tempname=ob.Ename;
			tempname.toLowerCase();
			for(int i=1;i<tempname.length();i++)
			{
				if (tempname.charAt(i)=" ")
					temp=tempname.charAt(i+1);
				    tempname=tempname(')
				}
		    }
		   tempnamecharAt(0)= tempname.charAt(0).toUppername();
		
		
		
		
		public static void main(String[] args) 
		{
			Scanner sc= new Scanner(System.in);
			int n=sc.nextInt();
		    Read(n);
		    sc.close();
		}
	
		}



