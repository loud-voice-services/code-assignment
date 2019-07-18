package com.loudvoiceservices.virtualbank.exceptions;

public class InvalidEmailException extends Exception {

	/**
	 * 
	 */
	private static final long serialVersionUID = 8466345153694830523L;

	public InvalidEmailException() {
		super("Invalid email, write a correct one.");
	}
	
}
