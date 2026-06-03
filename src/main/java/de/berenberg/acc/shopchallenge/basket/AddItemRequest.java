package de.berenberg.acc.shopchallenge.basket;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;

import java.util.UUID;

@Schema(description = "Request payload to add a product to a basket")
public record AddItemRequest(

        @NotNull
        @Schema(description = "ID of the product to add", example = "3fa85f64-5717-4562-b3fc-2c963f66afa6")
        UUID productId,

        @Min(1)
        @Schema(description = "Number of units to add", example = "2", minimum = "1")
        int quantity
) {}

