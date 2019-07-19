package com.loudvoiceservices.virtualbank;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

//(exclude = { SecurityAutoConfiguration.class })
@SpringBootApplication
public class VirtualbankApplication {

	public static void main(String[] args) {
		SpringApplication.run(VirtualbankApplication.class, args);
	}
	
}
