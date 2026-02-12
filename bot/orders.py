from bot.validators import validate_inputs, validate_notional

def create_order(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    # Set leverage (assignment bonus)
    client.set_leverage(symbol, leverage=10)

    # Get price for MARKET orders
    if order_type == "MARKET":
        price = client.get_mark_price(symbol)

    # Validate min notional
    validate_notional(quantity, price)

    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        order_data["price"] = price
        order_data["timeInForce"] = "GTC"

    return client.place_order(**order_data)
