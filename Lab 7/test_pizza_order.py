from hypothesis import given, strategies as st

from pizza_order import SIZES, TOPPINGS, pizza_inches, split_bill, toppings_price


@given(st.text())
def test_toppings_price_no_crash(s):
    total = toppings_price(s)
    assert isinstance(total, int)
    assert total >= 0


@given(st.text())
def test_pizza_inches_no_crash(s):
    size = pizza_inches(s)
    normalized = s.strip().upper()
    if normalized in SIZES:
        assert size == SIZES[normalized]
    else:
        assert size == 0


@given(st.text())
def test_split_bill_no_crash(s):
    amount = split_bill(s)
    assert isinstance(amount, (int, float))
    assert amount >= 0


@given(st.lists(st.sampled_from(sorted(TOPPINGS.keys())), unique=True))
def test_toppings_price_valid_toppings(toppings):
    csv = ",".join(toppings)
    expected = sum(TOPPINGS[topping] for topping in toppings)
    assert toppings_price(csv) == expected


@given(st.integers(min_value=1, max_value=1000), st.integers(min_value=1, max_value=20))
def test_split_bill_valid_input(total, people):
    expected = round(total / people, 2)
    assert split_bill(f"{total}/{people}") == expected
