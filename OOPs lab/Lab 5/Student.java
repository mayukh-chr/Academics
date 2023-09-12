package count;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;

public class Student {
    int registrationNumber;
    String fullName;
    Date dateOfJoining;
    short semester;
    float GPA;
    float CGPA;

    public Student(int registrationNumber, String fullName, Date dateOfJoining, short semester, float GPA, float CGPA) {
        this.registrationNumber = registrationNumber;
        this.fullName = fullName;
        this.dateOfJoining = dateOfJoining;
        this.semester = semester;
        this.GPA = GPA;
        this.CGPA = CGPA;
    }

    public void display() {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        System.out.println("Registration Number: " + registrationNumber);
        System.out.println("Full Name: " + fullName);
        System.out.println("Date of Joining: " + sdf.format(dateOfJoining));
        System.out.println("Semester: " + semester);
        System.out.println("GPA: " + GPA);
        System.out.println("CGPA: " + CGPA);
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student[] students = new Student[5];

        for (int i = 0; i < 5; i++) {
            System.out.println("Enter Student Details for Student " + (i + 1) + ":");
            System.out.print("Full Name: ");
            String fullName = scanner.nextLine();
            System.out.print("Date of Joining (dd/MM/yyyy): ");
            String dateStr = scanner.nextLine();
            Date dateOfJoining = null;
            try {
                SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
                dateOfJoining = sdf.parse(dateStr);
            } catch (Exception e) {
                System.out.println("Invalid date format. Using current date.");
                dateOfJoining = new Date();
            }
            System.out.print("Semester: ");
            short semester = scanner.nextShort();
            System.out.print("GPA: ");
            float GPA = scanner.nextFloat();
            System.out.print("CGPA: ");
            float CGPA = scanner.nextFloat();
            scanner.nextLine(); // Consume the newline character
            students[i] = new Student(2012 * 100 + (i + 1), fullName, dateOfJoining, semester, GPA, CGPA);
        }

        System.out.println("Student Records:");
        for (Student student : students) {
            student.display();
        }

        // Sorting by semester and CGPA
        Arrays.sort(students, (s1, s2) -> {
            if (s1.semester != s2.semester) {
                return s1.semester - s2.semester;
            } else {
                return Float.compare(s2.CGPA, s1.CGPA);
            }
        });

        System.out.println("Sorted by Semester and CGPA:");
        for (Student student : students) {
            student.display();
        }

        // Sorting by name
        Arrays.sort(students, (s1, s2) -> s1.fullName.compareToIgnoreCase(s2.fullName));

        System.out.println("Sorted by Name:");
        for (Student student : students) {
            student.display();
        }

        // List students by first character in name
        char searchChar = 'P';
        System.out.println("Students whose name starts with '" + searchChar + "':");
        for (Student student : students) {
            if (student.fullName.charAt(0) == searchChar || student.fullName.charAt(0) == Character.toLowerCase(searchChar)) {
                student.display();
            }
        }

        // List students by substring in name
        String searchString = "Kalingrao";
        System.out.println("Students whose name contains '" + searchString + "':");
        for (Student student : students) {
            if (student.fullName.contains(searchString)) {
                student.display();
            }
        }

        // Change full name to initials and family name
        for (Student student : students) {
            String[] nameParts = student.fullName.split(" ");
            StringBuilder newName = new StringBuilder();
            for (int i = 0; i < nameParts.length; i++) {
                if (i == nameParts.length - 1) {
                    newName.append(nameParts[i]);
                } else {
                    newName.append(nameParts[i].charAt(0)).append(". ");
                }
            }
            student.fullName = newName.toString();
        }

        System.out.println("Modified Student Records:");
        for (Student student : students) {
            student.display();
        }
    }
}
