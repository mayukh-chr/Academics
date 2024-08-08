package count;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;
	

public class Student {
	    int registrationNumber;
	    String fullName;
	    Date dateOfJoining;
	    short semester;
	    float gpa;
	    float cgpa;

	    // Parameterized constructor to create a student record
	    public Student(String fullName, Date dateOfJoining, short semester, float gpa, float cgpa) {
	        this.fullName = fullName;
	        this.dateOfJoining = dateOfJoining;
	        this.semester = semester;
	        this.gpa = gpa;
	        this.cgpa = cgpa;

	        // Calculate the registration number based on the year of joining
	        int year = dateOfJoining.getYear() + 1900;
	        int studentNumber = 80; // Assuming student number is provided as an argument
	        this.registrationNumber = year * 100 + studentNumber;
	    }

	    // Display the student record
	    public void display() {
	        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
	        System.out.println("Registration Number: " + registrationNumber);
	        System.out.println("Full Name: " + fullName);
	        System.out.println("Date of Joining: " + dateFormat.format(dateOfJoining));
	        System.out.println("Semester: " + semester);
	        System.out.println("GPA: " + gpa);
	        System.out.println("CGPA: " + cgpa);
	        System.out.println();
	    }

	    public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);
	        Student[] students = new Student[5];

	        for (int i = 0; i < students.length; i++) {
	            System.out.println("Enter Student " + (i + 1) + " Details:");

	            System.out.print("Full Name: ");
	            String fullName = scanner.nextLine();

	            System.out.print("Date of Joining (dd/MM/yyyy): ");
	            String dateStr = scanner.nextLine();
	            SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
	            Date dateOfJoining = null;
	            try {
	                dateOfJoining = dateFormat.parse(dateStr);
	            } catch (Exception e) {
	                System.out.println("Invalid date format. Please use dd/MM/yyyy.");
	                i--;
	                continue;
	            }

	            System.out.print("Semester: ");
	            short semester = scanner.nextShort();

	            System.out.print("GPA: ");
	            float gpa = scanner.nextFloat();

	            System.out.print("CGPA: ");
	            float cgpa = scanner.nextFloat();

	            scanner.nextLine(); // Consume the newline character

	            students[i] = new Student(fullName, dateOfJoining, semester, gpa, cgpa);
	        }

	        System.out.println("Student Records:");
	        for (Student student : students) {
	            student.display();
	        }

	        scanner.close();
	    }
	}


