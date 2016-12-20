package org.sgooty.warmup;

import java.util.Scanner;

public class diagonoalDifference {
	
	public static void main(String args[]) {
		
		System.out.println("Enter the length of 2-D array");
		Scanner in = new Scanner(System.in); 
		// Get the length of 2-D matrix 
		int n = in.nextInt(); 
		
		// Create a 2-D Array 
		int arr[][] = new int[n][n]; 
		
		// Enter the values in 2-D array
		
		for(int i=0; i< n; i++) { 
			for (int j=0; j<n;j++) { 
				arr[i][j] = in.nextInt();
			}
		}
		
		int lsum,rsum;
		lsum = rsum = 0; 
		
		for(int i=0; i< n; i++) { 
			for (int j=0; j<n;j++) { 
				if(i ==j ) { 
					lsum += arr[i][j];
				}
				
				if(j ==n -i-1) { 
					rsum += arr[i][j];
				}
			}
		}
		
		System.out.println(lsum-rsum);
	}

}
