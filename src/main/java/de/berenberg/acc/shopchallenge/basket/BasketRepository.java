package de.berenberg.acc.shopchallenge.basket;

import org.springframework.stereotype.Repository;

import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

import de.berenberg.acc.shopchallenge.basket.model.Basket;

/**
 * In-memory basket storage.  Baskets are created on demand.
 */
@Repository
public class BasketRepository {

    private final Map<UUID, Basket> store = new ConcurrentHashMap<>();

    /** Returns the basket for the given id, creating a new one if absent. */
    public Basket getOrCreate(UUID id) {
        return store.computeIfAbsent(id, Basket::new);
    }

    public Optional<Basket> findById(UUID id) {
        return Optional.ofNullable(store.get(id));
    }
}

