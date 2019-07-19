package com.loudvoiceservices.virtualbank;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import com.loudvoiceservices.virtualbank.domain.User;
import com.loudvoiceservices.virtualbank.exceptions.InvalidEmailException;
import com.loudvoiceservices.virtualbank.exceptions.UserAlreadyExistsException;
import com.loudvoiceservices.virtualbank.repositories.UserRepository;
import com.loudvoiceservices.virtualbank.services.UserService;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UserServiceTests {

	@Autowired
	private UserService service;
	
	@Autowired
	private UserRepository repository;
	
	@Test
	public void testCreateUser() {
		User user = new User();
		user.setEmail("algumusuario@test.com");
		user.setPassword("algumasenha");
		try {
			service.createUser(user);
		} catch(UserAlreadyExistsException e) {
			Assert.assertTrue(true);
		} catch(InvalidEmailException e) {
			Assert.assertTrue(true);
		} catch (Exception e) {
			Assert.assertTrue(false);
		}
		
		Assert.assertTrue(repository.findByEmail(user.getEmail()).isPresent());
	}
	
}
