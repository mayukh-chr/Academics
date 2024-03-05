package count;

public class Student {
	
	    private int studentId;
	    private String studentName;
	    private int age;
	    private double grade;

	    // Default constructor
	    public Student() {
	        // Initialize data members with default values
	        studentId = 0;
	        studentName = "";
	        age = 0;
	        grade = 0.0;
	    }

	    // Parameterized constructor
	    public Student(int studentId, String studentName, int age, double grade) {
	        this.studentId = studentId;
	        this.studentName = studentName;
	        this.age = age;
	        this.grade = grade;
	    }

	    // Display method
	    public void display() {
	        System.out.println("Student ID: " + studentId);
	        System.out.println("Student Name: " + studentName);
	        System.out.println("Age: " + age);
	        System.out.println("Grade: " + grade);
	    }

	    public static void main(String[] args) {
	        // Illustrating the usage of the class with complex objects
	        Student student1 = new Student(1, "Alice", 18, 90.5);
	        Student student2 = new Student(2, "Bob", 20, 85.0);
	        Student student3 = new Student();

	        // Display details of student1 and student2
	        student1.display();
	        student2.display();

	        // Display details of student3 (initialized with default values)
	        student3.display();
	    }
	}


