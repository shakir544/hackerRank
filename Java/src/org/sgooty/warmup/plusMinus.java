package org.sgooty.warmup;

import java.util.Scanner;

public class plusMinus {
	
	public static void main(String args[]) { 
		Scanner in = new Scanner(System.in); 
		int p,neg,zero; 
		p = neg =zero =0; 
		
		int n = in.nextInt();
        int arr[] = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
            
            if(arr[arr_i] >0)
        		p++; 
        	else if(arr[arr_i] < 0)
        		neg++;
        	else if(arr[arr_i] ==0)
        		zero++;
        }
          
        System.out.println((double)p/n);
        System.out.println((double)neg/n);
        System.out.println((double)zero/n);
	}

}
