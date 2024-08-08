package count;

public class Employee {
    private int employeeId;
    private String employeeName;
    private double salary;

    // Default constructor
    public Employee() {
        // Initialize data members with default values
        employeeId = 0;
        employeeName = "";
        salary = 0.0;
    }

    // Parameterized constructor
    public Employee(int employeeId, String employeeName, double salary) {
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.salary = salary;
    }

    // Display method
    public void display() {
        System.out.println("Employee ID: " + employeeId);
        System.out.println("Employee Name: " + employeeName);
        System.out.println("Salary: $" + salary);
    }

    public static void main(String[] args) {
        // Illustrating the usage of the class with employee objects
        Employee employee1 = new Employee(1, "Alice", 50000.0);
        Employee employee2 = new Employee(2, "Bob", 60000.0);
        Employee employee3 = new Employee();

        // Display details of employee1 and employee2
        System.out.println("Details of Employee 1:");
        employee1.display();

        System.out.println("\nDetails of Employee 2:");
        employee2.display();

        // Display details of employee3 (initialized with default values)
        System.out.println("\nDetails of Employee 3:");
        employee3.display();
    }
}

