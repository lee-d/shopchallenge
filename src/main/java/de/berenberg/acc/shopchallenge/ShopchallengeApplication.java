package de.berenberg.acc.shopchallenge;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@OpenAPIDefinition(
		info = @Info(
				title = "Shop Challenge API",
				version = "1.0",
				description = "REST API simulating a web shop: browse products, manage baskets, view net & gross totals."
		)
)
@SpringBootApplication
public class ShopchallengeApplication {

	public static void main(String[] args) {
		SpringApplication.run(ShopchallengeApplication.class, args);
	}

}
