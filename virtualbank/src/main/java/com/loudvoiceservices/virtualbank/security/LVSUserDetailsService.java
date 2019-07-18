package com.loudvoiceservices.virtualbank.security;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

import com.loudvoiceservices.virtualbank.domain.User;
import com.loudvoiceservices.virtualbank.repositories.UserRepository;

@Component
public class LVSUserDetailsService implements UserDetailsService {

	@Autowired
	private UserRepository repository;

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
		Optional<User> op = repository.findByEmail(username);
		if (!op.isPresent()) {
			throw new UsernameNotFoundException("User not found.");
		}

		User lvsUser = op.get();

		List<SimpleGrantedAuthority> authorities = new ArrayList<>();
		authorities.add(new SimpleGrantedAuthority("ADMIN"));

		return new org.springframework.security.core.userdetails.User(lvsUser.getEmail(), lvsUser.getPassword(),
				authorities);
	}

}
