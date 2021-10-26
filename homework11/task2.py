from typing import Callable


class Order:
    """Receives price, and, optionally, discount strategy.
    If discount strategy exists, returns its value through
    final price method."""
    def __init__(self, price: int, discount_strategy: Callable = None) -> None:
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self) -> int:
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        price_with_discount = self.price - discount
        if price_with_discount < 0:
            return 0
        return price_with_discount


def morning_discount(order: Order) -> float:
    """Counts discount, calling price from Order class."""
    return order.price * 0.25


def elder_discount(order: Order) -> float:
    """Counts discount, calling price from Order class."""
    return order.price * 0.9
