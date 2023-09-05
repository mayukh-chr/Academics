package count;
import java.util.*;

class Lab_4_Ex_1 { 
	String name;
	String accNumber;
	String accType;
	double balance;
	static int interestRate;
	
	public Lab_4_Ex_1() {
		name = "default name";
		accNumber = "-1";
        accType = "inv";
        balance = -1.0;
	}
	
	public Lab_4_Ex_1(String depositorName, String accountNumber, String accountType, double initialBalance) {
        this.name = depositorName;
        this.accNumber = accountNumber;
        this.accType = accountType;
        this.balance = initialBalance;
    }
	
	public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited $" + amount + ". New balance: $" + balance);
        } else {
            System.out.println("Invalid deposit amount. Please enter a positive value.");
        }
    }
	
	public void withdraw(double amount) {
        double minimumBalance = 100.0; 
        if (amount > 0) {
            if (balance - amount >= minimumBalance) {
                balance -= amount;
                System.out.println("Withdrew $" + amount + ". New balance: $" + balance);
            } else {
                System.out.println("Insufficient balance to make the withdrawal.");
            }
        } else {
            System.out.println("Invalid withdrawal amount. Please enter a positive value.");
        }
    }
	
	public void display() {
        System.out.println("Account Details:");
        System.out.println("Depositor Name: " + name);
        System.out.println("Account Number: " + accNumber);
        System.out.println("Account Type: " + accType);
        System.out.println("Balance: $" + balance);
    }
	
	public static void displayInterestRate() {
        System.out.println("Current Interest Rate: " + (interestRate * 100) + "%");
    }
	
	public static void main(String[] args) {
		Lab_4_Ex_1 Acc=new Lab_4_Ex_1();
	        Scanner sc = new Scanner(System.in);
	        int choice,i=0 ;
	        double amount=0;
	        
	        System.out.print("1. Deposit \n2. Withdraw\n3. display\n4. exit: ");
	        while(i==0){
	        choice=sc.nextInt();
	        switch(choice){
	            case 1:
	            	System.out.print("Enter amount: ");
	            	amount = sc.nextDouble();
	            Acc.deposit(amount);
	            break;
	            case 2:
	            	System.out.print("Enter amount: ");
	            	amount = sc.nextDouble();
	            Acc.withdraw(amount);
	            break;
	            case 3:
	            Acc.display();
	            break;
	            case 4:
	            i=1;
	            break;
	            

	        }

	        Lab_4_Ex_1.displayInterestRate();
        
        sc.close();
    }

	}
}
	

