import yfinance as yf

portfolio = {}

def add_stock(symbol, shares, purchase_price):
    portfolio[symbol.upper()] = {
        "shares": shares,
        "purchase_price": purchase_price
    }
    print(f"✅ Added {shares} shares of {symbol.upper()} at ${purchase_price} each.")

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑 Removed {symbol} from portfolio.")
    else:
        print("⚠️ Stock not found.")

def show_portfolio():
    print("\n📊 Your Stock Portfolio:")
    if not portfolio:
        print("No stocks in portfolio.")
        return

    total_value = 0
    total_cost = 0

    for symbol, data in portfolio.items():
        stock = yf.Ticker(symbol)
        current_price = stock.info['regularMarketPrice']
        shares = data["shares"]
        cost = shares * data["purchase_price"]
        value = shares * current_price
        gain = value - cost

        total_cost += cost
        total_value += value

        print(f"\n🔹 {symbol}")
        print(f"   Shares: {shares}")
        print(f"   Purchase Price: ${data['purchase_price']}")
        print(f"   Current Price:  ${current_price:.2f}")
        print(f"   Value: ${value:.2f} | Gain/Loss: ${gain:.2f}")

    print(f"\n💼 Total Portfolio Value: ${total_value:.2f}")
    print(f"💰 Total Investment Cost: ${total_cost:.2f}")
    print(f"📈 Net Gain/Loss: ${total_value - total_cost:.2f}")

def menu():
    while True:
        print("\n📍 Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol
