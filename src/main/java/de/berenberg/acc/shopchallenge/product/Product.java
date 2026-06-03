package de.berenberg.acc.shopchallenge.product;

import lombok.Value;

import java.util.UUID;

/**
 * Represents a product in the shop catalogue.
 * Fields: id, name, netPrice.
 */
@Value
public class Product {

    UUID id;
    String name;
    double netPrice;
}


