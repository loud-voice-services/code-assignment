package com.loudvoiceservices.virtualbank.exceptions;

public class UserNotFoundException extends Exception {
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1098444802739906237L;

	public UserNotFoundException() {
		super("User not found, enter in contact with support.");
	}
}
