package org.sgooty.implementation;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class angryProfessor {
	
	public static void main(String args[]) { 
		
		Scanner in = new Scanner(System.in); 

		int T = in.nextInt();  // Number of test cases
		
		
		for(int i =0; i< T; i++){ 
			int n = in.nextInt(); // n - number of students in class
			int k = in.nextInt(); // Threshold of K
			int min=0;
			int arr[] = new int[n]; 
			for(int j=0;j<n;j++){ 
				arr[j] = in.nextInt(); 
				
				if(arr[j] <= 0) { 
					min++;
				}
			}
			if(min >= k)
				System.out.println("NO");
			else 
				System.out.println("YES");
		}
	}

}
