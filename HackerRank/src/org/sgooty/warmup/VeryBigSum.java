package org.sgooty.warmup;

import java.util.Scanner;

public class VeryBigSum {
	
	// Calculate the sum 
	public static long veryBigSum(long[] arr) { 
		int len = arr.length; 
		long sum=0; 
		for(int i=0; i < len; i++) { 
			sum += arr[i]; 
		}
		
		return sum;
	}
	
	// Get the input from the user
	public static long[] getInputFromUser(){ 
		Scanner scan = new Scanner(System.in); 
		int len = Integer.parseInt(scan.next());
		int i =0;
		long[] arr = new long[10]; 
		while (i <len) {
			arr[i] = Long.parseLong(scan.next());
			i++;
		}
		return arr;
		
	}
	
	// Get the inputs from the user alternate method
	public static long[] getInputFromUserMenthod2() { 
		Scanner scan = new Scanner(System.in); 
		int len = Integer.parseInt(scan.next());
		
		String[] strings = scan.nextLine().split(" ");
		long[] array = new long[len]; 
		
		for(int i=0;i<len;i++){ 
			array[i] = Long.parseLong(strings[i]);
		}
		
		return array; 
	}
	public static void main(String args[]) { 
		
		/*You are given an array of integers of size NN. You need to print the sum of the elements 
		in the array, keeping in mind that some of those integers may be quite large.*/
		 Scanner scan = new Scanner(System.in); 
	        int len = Integer.parseInt(scan.nextLine()); 
	        String[] str = scan.nextLine().split(" "); 
	        long[] arr = new long[len]; 
	        long sum =0; 
	        for(int i=0; i<len; i++) { 
	        arr[i] = Long.parseLong(str[i]);
	            sum += arr[i]; 
	        }
	        System.out.println(sum);
		
	
	}

}
