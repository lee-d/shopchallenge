package de.berenberg.acc.shopchallenge.basket.model;

import java.util.UUID;

import lombok.Value;

/**
 * A single line item inside a basket.
 * Fields: productId, quantity.
 */
@Value
public class BasketItem {
    UUID productId;
    int quantity;
}


