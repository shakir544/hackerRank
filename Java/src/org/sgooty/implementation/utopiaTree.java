package org.sgooty.implementation;

import java.util.Scanner;

public class utopiaTree {
	public static void main(String args[]){ 
		
		
		
		Scanner in = new Scanner(System.in);
		int T = in.nextInt(); 
		for(int i=0;i<T;i++){ 
			int n = in.nextInt();
			System.out.println(getHeight(n));
		}
	}
		
		
		public static int getHeight(int treeCycles){ 
			
			int height = 1; 
			for(int i =0; i < treeCycles; i++){ 
				if(i%2 ==0)
					height *=2;
				else 
					height +=1; 
			}
			return height; 
			
		}
	

}
