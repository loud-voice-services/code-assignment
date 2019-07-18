package com.loudvoiceservices.virtualbank.services;

import java.util.Optional;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import com.loudvoiceservices.virtualbank.domain.User;
import com.loudvoiceservices.virtualbank.exceptions.InvalidEmailException;
import com.loudvoiceservices.virtualbank.exceptions.NegativeNumberException;
import com.loudvoiceservices.virtualbank.exceptions.UserAlreadyExistsException;
import com.loudvoiceservices.virtualbank.exceptions.UserNotFoundException;
import com.loudvoiceservices.virtualbank.repositories.UserRepository;

@Service
@Transactional
public class UserService {

	@Autowired
	public UserRepository repository;

	/**
	 * Creates a new user on database.
	 *  
	 * @param user (User with email and password)
	 * @throws UserAlreadyExistsException in case the user already exists
	 * @throws InvalidEmailException      in case of wrong email.
	 */
	public void createUser(User user) throws Exception {
		if (repository.findByEmail(user.getEmail()).isPresent()) {
			throw new UserAlreadyExistsException();
		}

		String regex = "^[\\w-_\\.+]*[\\w-_\\.]\\@([\\w]+\\.)+[\\w]+[\\w]$";
		if (!user.getEmail().matches(regex)) {
			throw new InvalidEmailException();
		}

		repository.save(user);
	}

	/**
	 * Withdraw an amount from the database.
	 * 
	 * @param amount
	 * @throws Exception
	 */
	public void withDraw(Double amount) throws Exception {
		User savedUser = getLoggedUser();
		validateAmount(amount);

		Double actualAmount = savedUser.getAmount();
		if (actualAmount - amount < 0) {
			throw new RuntimeException("You can't withdraw more than you have. Actual amount is " + actualAmount);
		} else {
			savedUser.setAmount(actualAmount - amount);
			repository.save(savedUser);
		}
	}

	/**
	 * Deposits an amount into the database for the user.
	 * 
	 * @param amount
	 * @throws Exception
	 */
	public void deposit(Double amount) throws Exception {
		User savedUser = getLoggedUser();
		validateAmount(amount);
		Double actualAmount = savedUser.getAmount();
		savedUser.setAmount(actualAmount + amount);
		repository.save(savedUser);
	}
	
	/**
	 * Show user amount of currency stored..
	 * 
	 * @param amount
	 * @throws Exception
	 */
	public String balance() throws Exception {
		User savedUser = getLoggedUser();
		return "Your balance is: " + String.valueOf(savedUser.getAmount());
	}

	/**
	 * Validate if the user exists on database.
	 * 
	 * @param user
	 * @return
	 * @throws UserNotFoundException
	 */
	private User validateUser(User user) throws UserNotFoundException {
		Optional<User> op = repository.findByEmail(user.getEmail());
		if (!op.isPresent()) {
			throw new UserNotFoundException();
		}
		return op.get();
	}

	/**
	 * Validates if the number is positive, if not, throws a NegativeNumberException
	 * 
	 * @param amount Double value that will be used.
	 * @throws NegativeNumberException
	 */
	private void validateAmount(Double amount) throws NegativeNumberException {
		if (amount < 0) {
			throw new NegativeNumberException();
		}
	}

	/**
	 * Returns the authenticated user.
	 * 
	 * @return User authenticated User.
	 * @throws UserNotFoundException if can't find the user on data base.
	 */
	private User getLoggedUser() throws UserNotFoundException {
		User loggedUser = new User();
		Object principal = SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		if (principal instanceof UserDetails) {
			loggedUser.setEmail(((UserDetails) principal).getUsername());
		} else {
			loggedUser.setEmail(principal.toString());
		}

		return validateUser(loggedUser);
	}

}
