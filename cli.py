import argparse
from bot.client import BinanceClient
from bot.orders import create_order

API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT")

    args = parser.parse_args()

    try:
        client = BinanceClient(API_KEY, API_SECRET)

        print("\n📌 Order Request Summary")
        for k, v in vars(args).items():
            print(f"{k}: {v}")

        response = create_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n✅ Order Placed Successfully")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))


if __name__ == "__main__":
    main()
