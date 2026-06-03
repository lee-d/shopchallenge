package de.berenberg.acc.shopchallenge.basket;

import de.berenberg.acc.shopchallenge.basket.model.Basket;
import de.berenberg.acc.shopchallenge.product.Product;
import de.berenberg.acc.shopchallenge.product.ProductRepository;
import jakarta.annotation.PostConstruct;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.UUID;

/**
 * Populates a ready-to-use test basket on application start-up.
 *
 * <p>The basket can be fetched via:
 * <pre>GET /baskets/00000000-0000-0000-0000-000000000001</pre>
 */
@Component
public class DataInitializer {

    /** Fixed UUID so the test basket is always reachable at the same address. */
    public static final UUID TEST_BASKET_ID =
            UUID.fromString("00000000-0000-0000-0000-000000000001");

    private final BasketRepository basketRepository;
    private final ProductRepository productRepository;

    public DataInitializer(BasketRepository basketRepository,
                           ProductRepository productRepository) {
        this.basketRepository = basketRepository;
        this.productRepository = productRepository;
    }

    @PostConstruct
    public void init() {
        List<Product> products = productRepository.findAll();

        Basket testBasket = basketRepository.getOrCreate(TEST_BASKET_ID);
        testBasket.addItem(products.get(0).getId(), 2);  // 2× first product
        testBasket.addItem(products.get(1).getId(), 1);  // 1× second product
        testBasket.addItem(products.get(2).getId(), 3);  // 3× third product
    }
}

