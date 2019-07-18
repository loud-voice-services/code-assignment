package com.loudvoiceservices.virtualbank.exceptions;

public class UserAlreadyExistsException extends Exception {
	
	/**
	 * 
	 */
	private static final long serialVersionUID = -8842421550861851660L;

	public UserAlreadyExistsException() {
		super("User already exists, use other email.");
	}
}
