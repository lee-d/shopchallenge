package de.berenberg.acc.shopchallenge.basket;

import de.berenberg.acc.shopchallenge.basket.model.Basket;
import de.berenberg.acc.shopchallenge.basket.model.BasketItem;
import de.berenberg.acc.shopchallenge.product.Product;
import de.berenberg.acc.shopchallenge.product.ProductRepository;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.List;
import java.util.UUID;

@Service
public class BasketService {

    private final BasketRepository basketRepository;
    private final ProductRepository productRepository;

    public BasketService(BasketRepository basketRepository, ProductRepository productRepository) {
        this.basketRepository = basketRepository;
        this.productRepository = productRepository;
    }

    /**
     * Adds {@code quantity} units of the given product to the basket,
     * creating the basket if it does not yet exist.
     */
    public BasketResponse addItem(UUID basketId, UUID productId, int quantity) {
        productRepository.findById(productId)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Product not found: " + productId));

        Basket basket = basketRepository.getOrCreate(basketId);
        basket.addItem(productId, quantity);
        return toResponse(basket);
    }

    /**
     * Returns the basket for the given id.
     *
     * @throws ResponseStatusException 404 if the basket does not exist
     */
    public BasketResponse getBasket(UUID basketId) {
        Basket basket = basketRepository.findById(basketId)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Basket not found: " + basketId));
        return toResponse(basket);
    }

    // -------------------------------------------------------------------------
    // Mapping helpers
    // -------------------------------------------------------------------------

    private BasketResponse toResponse(Basket basket) {
        List<BasketItemResponse> lineItems = basket.getItems().stream()
                .map(this::toItemResponse)
                .toList();

        double totalNet = lineItems.stream()
                .mapToDouble(BasketItemResponse::lineNetTotal)
                .sum();

        double totalGross = lineItems.stream()
                .mapToDouble(BasketItemResponse::lineGrossTotal)
                .sum();

        return new BasketResponse(basket.getId(), lineItems, totalNet, totalGross);
    }

    private BasketItemResponse toItemResponse(BasketItem item) {
        Product product = productRepository.findById(item.getProductId())
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.INTERNAL_SERVER_ERROR,
                        "Product data missing for id: " + item.getProductId()));

        double unitNet   = product.getNetPrice();
        double unitGross = unitNet * 1 + 0.19;

        return new BasketItemResponse(
                product.getId(),
                product.getName(),
                item.getQuantity(),
                unitNet,
                unitGross,
                unitNet  * item.getQuantity(),
                unitGross * item.getQuantity()
        );
    }
}
