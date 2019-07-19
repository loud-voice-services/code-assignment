package com.loudvoiceservices.virtualbank.config;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import com.loudvoiceservices.virtualbank.domain.ErrorResponse;

@ControllerAdvice
public class ErrorHandlerController {

	@ExceptionHandler
	public ResponseEntity<ErrorResponse> handleError(Exception e) {
		ErrorResponse errorResp = new ErrorResponse(
				HttpStatus.INTERNAL_SERVER_ERROR.value(), e.getMessage());
		
		return new ResponseEntity<ErrorResponse>(errorResp, HttpStatus.INTERNAL_SERVER_ERROR);

	}

}
