package com.loudvoiceservices.virtualbank.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.loudvoiceservices.virtualbank.domain.User;

public interface UserRepository extends JpaRepository<User, Long> {
	
	 public Optional<User>findByEmail(String email);

}
