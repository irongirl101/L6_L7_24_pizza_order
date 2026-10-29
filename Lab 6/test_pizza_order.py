import pytest
from pizza_order import pizza_price, order_discount, delivery_status


@pytest.mark.parametrize(
    "size,toppings,is_cheese_burst,expected",
    [
        ("small", 0, False, 200),
        ("medium", 2, False, 430),
        ("large", 5, False, 680),
        ("large", 0, True, 600),
    ],
)
def test_pizza_price_valid_orders(size, toppings, is_cheese_burst, expected):
    assert pizza_price(size, toppings, is_cheese_burst) == expected


def test_pizza_price_invalid_size_raises_value_error():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra large", 1, False)


def test_pizza_price_invalid_toppings_raises_value_error():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_pizza_price_small_cheese_burst_raises_value_error():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)


@pytest.mark.parametrize(
    "order_total,day,is_student,expected",
    [
        (250, "monday", False, 0),
        (500, "tuesday", False, 250),
        (500, "tuesday", True, 300),
        (600, "saturday", False, 0),
        (600, "saturday", True, 50),
        (500, "monday", False, 50),
        (500, "monday", True, 100),
    ],
)
def test_order_discount_cases(order_total, day, is_student, expected):
    assert order_discount(order_total, day, is_student) == expected


@pytest.mark.parametrize(
    "minutes_taken,distance_km,expected",
    [
        (20, 3, "on time"),
        (35, 5, "late"),
        (50, 5, "free pizza"),
        (20, 15, "not deliverable"),
    ],
)
def test_delivery_status_cases(minutes_taken, distance_km, expected):
    assert delivery_status(minutes_taken, distance_km) == expected
