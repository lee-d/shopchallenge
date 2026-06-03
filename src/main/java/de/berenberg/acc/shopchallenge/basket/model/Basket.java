package de.berenberg.acc.shopchallenge.basket.model;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/**
 * A shopping basket belonging to a specific customer session.
 */
public class Basket {

    private final UUID id;
    private final List<BasketItem> items = new ArrayList<>();

    public Basket(UUID id) {
        this.id = id;
    }

    public UUID getId() {
        return id;
    }

    public List<BasketItem> getItems() {
        return List.copyOf(items);
    }

    /**
     * Adds the given quantity of a product.  If the product is already in the
     * basket, the quantities are merged.
     */
    public void addItem(UUID productId, int quantity) {
        if (quantity <= 0) {
            throw new IllegalArgumentException("Quantity must be greater than 0");
        }
        for (int i = 0; i < items.size(); i++) {
            if (items.get(i).getProductId().equals(productId)) {
                items.set(i, new BasketItem(productId, quantity));
                return;
            }
        }
        items.add(new BasketItem(productId, quantity));
    }
}

