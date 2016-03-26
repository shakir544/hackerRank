package org.sgooty.implementation;

import java.util.Scanner;

public class findDigits {
	public static void main(String args[]){ 
		
		Scanner in = new Scanner(System.in); 
		int T = in.nextInt(); // Test cases 
		
		for(int i =0; i <T;i++){ 
			String n = in.next();
			System.out.println(digitCounts(n));
			
		}
	}
	
	public static int digitCounts(String number){ 
		int len = number.length();
		int digits =0; 
		int num =Integer.parseInt(number);
		for(int i=0; i<len; i++){ 
			int div = number.charAt(i)-48;
			if(div !=0 && num%div==0)
				digits++; 
		}
		return digits;
	}
	

}
