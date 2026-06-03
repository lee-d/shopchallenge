package de.berenberg.acc.shopchallenge.basket;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@RestController
@RequestMapping("/api/baskets")
@Tag(name = "Baskets", description = "Manage shopping baskets")
public class BasketController {

    private final BasketService basketService;

    public BasketController(BasketService basketService) {
        this.basketService = basketService;
    }

    @GetMapping("/{id}")
    @Operation(
            summary = "Get basket by ID",
            description = "Returns the basket with all line items, per-product net & gross prices, and overall totals.")
    public BasketResponse getBasket(
            @Parameter(description = "Basket UUID", example = "123e4567-e89b-12d3-a456-426614174000")
            @PathVariable UUID id) {
        return basketService.getBasket(id);
    }

    @PostMapping("/{id}/items")
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(
            summary = "Add a product to the basket",
            description = "Adds the specified quantity of a product to the basket.  "
                    + "The basket is created automatically if it does not yet exist.  "
                    + "Calling this endpoint again for the same product merges the quantities.")
    public BasketResponse addItem(
            @Parameter(description = "Basket UUID", example = "123e4567-e89b-12d3-a456-426614174000")
            @PathVariable UUID id,
            @RequestBody AddItemRequest request) {
        return basketService.addItem(id, request.productId(), request.quantity());
    }
}

