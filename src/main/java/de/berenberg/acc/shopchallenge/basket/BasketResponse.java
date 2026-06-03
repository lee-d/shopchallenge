package de.berenberg.acc.shopchallenge.basket;

import io.swagger.v3.oas.annotations.media.Schema;

import java.util.List;
import java.util.UUID;

@Schema(description = "A shopping basket with all line items and totals")
public record BasketResponse(

        @Schema(description = "Basket ID (same as the path parameter)")
        UUID id,

        @Schema(description = "All products currently in the basket")
        List<BasketItemResponse> items,

        @Schema(description = "Sum of all line net totals", example = "2637.90")
        double totalNet,

        @Schema(description = "Sum of all line gross totals", example = "3138.90")
        double totalGross
) {}

