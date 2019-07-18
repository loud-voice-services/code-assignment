package com.loudvoiceservices.virtualbank.resources;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoudVoiceResource {
	@GetMapping(value = "/")
	public String index() {
		return "Welcome to the VirtualBank Rest Application.";
	}
	
	@GetMapping(value = "/private")
	public String account() {
		return "You accessed private area.";
	}
}
