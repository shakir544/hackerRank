package org.sgooty.warmup;

import java.util.Scanner;

//Your teacher has given you the task of drawing a staircase structure. 
//Being an expert programmer, you decided to make a program to draw it for you instead. 
//Given the required height, can you print a staircase as shown in the example?

public class staircase {
	
	public static void main(String args[]) { 
		Scanner in = new Scanner(System.in);
		
		int height = in.nextInt();
		
		for(int i=0;i<height;i++){ 
			for(int j=0;j<height;j++) { 
				if(j < height-1-i)
				System.out.print(" ");
				else
					System.out.print("#");
			}
			System.out.println();
		}
	}

}
