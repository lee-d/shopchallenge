package de.berenberg.acc.shopchallenge.product;

import org.springframework.stereotype.Repository;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;

/**
 * In-memory product catalogue.  Pre-populated with sample products.
 */
@Repository
public class ProductRepository {

    private final Map<UUID, Product> store = new LinkedHashMap<>();

    public ProductRepository() {
        add("10000000-0000-0000-0000-000000000000", "Laptop Pro 15",             1299.00);
        add("20000000-0000-0000-0000-000000000000", "Mechanical Keyboard",          89.99);
        add("30000000-0000-0000-0000-000000000000", "USB-C Hub 7-in-1",             34.99);
        add("40000000-0000-0000-0000-000000000000", "Organic Coffee Beans",         12.50);
        add("50000000-0000-0000-0000-000000000000", "Programming Book",             39.90);
        add("60000000-0000-0000-0000-000000000000", "27\" 4K Monitor",             549.00);
        add("70000000-0000-0000-0000-000000000000", "Noise-Cancelling Headphones", 249.00);
    }

    private void add(String uuid, String name, double netPrice) {
        Product p = new Product(UUID.fromString(uuid), name, netPrice);
        store.put(p.getId(), p);
    }

    public List<Product> findAll() {
        return List.copyOf(store.values());
    }

    public Optional<Product> findById(UUID id) {
        return Optional.ofNullable(store.get(id));
    }
}

