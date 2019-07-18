package com.loudvoiceservices.virtualbank.resources;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.loudvoiceservices.virtualbank.domain.User;
import com.loudvoiceservices.virtualbank.services.UserService;

@RestController
@RequestMapping("/accounts")
public class UserResource {
	
	@Autowired
	private UserService service;
	

	
	@RequestMapping(value = "", method = RequestMethod.POST, consumes = {"application/x-www-form-urlencoded"})
	public ResponseEntity<?> create(@RequestParam(name = "email") String email, 
			@RequestParam(name = "password") String password) throws Exception {
		User user = new User();
		user.setEmail(email);
		user.setPassword(password);
		service.createUser(user);
		return new ResponseEntity<>(HttpStatus.CREATED);
	}
	
	
	@RequestMapping(value = "/deposit", method = RequestMethod.POST, consumes = {"application/x-www-form-urlencoded"})
	public ResponseEntity<?> deposit(@RequestParam(name = "value") Double amount) throws Exception {
		service.deposit(amount);
		return new ResponseEntity<>(HttpStatus.OK);
	}
	
	@RequestMapping(value = "/withdraw", method = RequestMethod.POST, consumes = {"application/x-www-form-urlencoded"})
	public ResponseEntity<?> withdraw(@RequestParam(name = "value") Double amount) throws Exception {	
		service.withDraw(amount);
		return new ResponseEntity<>(HttpStatus.OK);
	}
	
	@GetMapping(value = "/accounts/balance")
	public String checkBalance() throws Exception {
		return service.balance();
	}

}
