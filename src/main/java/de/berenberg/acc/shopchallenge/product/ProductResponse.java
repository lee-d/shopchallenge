package de.berenberg.acc.shopchallenge.product;

import io.swagger.v3.oas.annotations.media.Schema;

import java.util.UUID;

@Schema(description = "A product available in the shop")
public record ProductResponse(

        @Schema(description = "Unique product ID", example = "3fa85f64-5717-4562-b3fc-2c963f66afa6")
        UUID id,

        @Schema(description = "Display name of the product", example = "Laptop Pro 15\"")
        String name,

        @Schema(description = "Net price (excl. VAT) in EUR", example = "999.00")
        double netPrice,

        @Schema(description = "Gross price (incl. VAT) in EUR", example = "1188.81")
        double grossPrice
) {

    public static ProductResponse from(Product p) {
        double gross = p.getNetPrice() * (1 + 0.19);
        return new ProductResponse(p.getId(), p.getName(), p.getNetPrice(), gross);
    }
}

