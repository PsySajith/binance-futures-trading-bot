MIN_NOTIONAL = 100


def validate_inputs(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT order")


def validate_notional(quantity, price):
    notional = quantity * price
    if notional < MIN_NOTIONAL:
        raise ValueError(
            f"Order notional {notional:.2f} is below minimum {MIN_NOTIONAL} USDT"
        )


def validate_limit_price(side, limit_price, mark_price):
    if side == "BUY" and limit_price >= mark_price:
        raise ValueError(
            f"BUY LIMIT price must be below current price ({mark_price})"
        )
    if side == "SELL" and limit_price <= mark_price:
        raise ValueError(
            f"SELL LIMIT price must be above current price ({mark_price})"
        )
