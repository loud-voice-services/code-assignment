package com.loudvoiceservices.virtualbank.exceptions;

public class NegativeNumberException extends Exception {
	/**
	 * 
	 */
	private static final long serialVersionUID = 197394446091874140L;

	public NegativeNumberException() {
		super("Number cannot be negative");
	}
}
