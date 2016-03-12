package org.sgooty.warmup;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;


public class TimeCoversion {
	
	// Given a time in AM/PM format, convert it to military (24-hour) time.
	
	public static void main(String args[]) throws ParseException { 
        SimpleDateFormat outputFormat = new SimpleDateFormat("HH:mm:ssa"); 
        SimpleDateFormat inputFormat = new SimpleDateFormat("hh:mm:ss"); 
        
        Scanner scan = new Scanner(System.in); 
        System.out.println(outputFormat.format(inputFormat.parse(scan.next())));
	}



}
