package count;

public class Lab_2_Ex_5 {
	public static void main(String[] args) {
		
		
		int arr [][] = new int[10][10];
		
		for(int i=0; i<10; i++) {
			for (int j =0; j<10 ; j++) {
				arr[i][j] = i+j;
			}
		}
		
		for(int i =0; i<10;i++) {
			for (int j =0; j<= i; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
		
	}
}
