package com.loudvoiceservices.virtualbank.config;

import java.util.ArrayList;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.service.VendorExtension;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@EnableSwagger2
@Configuration
public class SwaggerConfig {

	@Bean
	public Docket productApi() {
		
		return new Docket(DocumentationType.SWAGGER_2)
				.select()
				.apis(RequestHandlerSelectors.basePackage("com.loudvoiceservices.virtualbank.resources"))
				.paths(PathSelectors.any())
				.build()
				.apiInfo(apiInfo());
	}
	
	@SuppressWarnings("rawtypes")
	private ApiInfo apiInfo() {
		return new ApiInfo(
				"LOUD VOICE SERVICES BANK", 
				"Application test to get a new job.", 
				"1.0", 
				"Some terms of service.", 
				new Contact("Joao Paulo Cotrim","blank","joaopaulo.cotrim.arruda@gmail.com"), 
				"Apache 2.0", "http://www.apache.org/licenses/LICENSE-2.0", 
	              new ArrayList<VendorExtension>()
	              );
	}
	
}
