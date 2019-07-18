package com.loudvoiceservices.virtualbank.security;

import org.springframework.security.crypto.password.PasswordEncoder;

public class LVSPasswordEncoder implements PasswordEncoder {

	@Override
	public String encode(CharSequence rawPassword) {
		return String.valueOf(rawPassword);
	}

	@Override
	public boolean matches(CharSequence rawPassword, String encodedPassword) {
		if (encodedPassword == null) {
			return false;
		}
		
		if (rawPassword == null) {
			return false;
		}
		
		return encodedPassword.equals(encode(rawPassword));
	}

}
