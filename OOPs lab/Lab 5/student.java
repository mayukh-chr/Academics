package aryannayaklab5;

import java.util.Scanner;

public class student2{
		
		short sem;
		String name;
		String date;
		int regno;
		float gpa;
		float cgpa;
		
		student2(String name,int regno, String date,short sem,float gpa,float cgpa)
		{
			this.name=name;
			this.regno=regno;
			this.sem=sem;
			this.date=date;
			this.cgpa=cgpa;
			this.gpa=gpa;}
		
		public void  insert(student2 []record)
		{  
	     Scanner sc=new Scanner(System.in);
         System.out.println("enter the number of record");
	     int n=sc.nextInt();
		for(int i=0;i<n;i++) {
			System.out.println("enter your name");
		    record[i].name=sc.next();
			System.out.println("enter the regno ");
			record[i].regno=sc.nextInt();
			System.out.println("Enter cgpa ");
			record[i].cgpa=sc.nextFloat();
			System.out.println("Enter gpa ");
			record[i].gpa=sc.nextFloat();
			System.out.println("enter date");
			record[i].date=sc.next();
           }
		}
		
      public void  display(student[]record)
      {
    	 for(inti=0)
      }
