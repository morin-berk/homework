from homework11.task2 import Order, elder_discount, morning_discount


def test_morning_discount():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75


def test_elder_discount():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
