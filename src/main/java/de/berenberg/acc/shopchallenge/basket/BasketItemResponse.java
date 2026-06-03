package de.berenberg.acc.shopchallenge.basket;

import io.swagger.v3.oas.annotations.media.Schema;

import java.util.UUID;

@Schema(description = "One line item inside a basket")
public record BasketItemResponse(

        @Schema(description = "Product ID")
        UUID productId,

        @Schema(description = "Product name", example = "Laptop Pro 15\"")
        String productName,

        @Schema(description = "Number of units", example = "2")
        int quantity,

        @Schema(description = "Net unit price (excl. VAT)", example = "1299.00")
        double unitNetPrice,

        @Schema(description = "Gross unit price (incl. VAT)", example = "1545.81")
        double unitGrossPrice,

        @Schema(description = "Line total net (unitNetPrice × quantity)", example = "2598.00")
        double lineNetTotal,

        @Schema(description = "Line total gross (unitGrossPrice × quantity)", example = "3091.62")
        double lineGrossTotal
) {}

