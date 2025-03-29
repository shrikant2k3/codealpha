import yfinance as yf

# Portfolio dictionary to store stock data
portfolio = {}

# Function to add stock
def add_stock(symbol, quantity, buy_price):
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
        portfolio[symbol]['buy_price'] = (portfolio[symbol]['buy_price'] + buy_price) / 2
    else:
        portfolio[symbol] = {'quantity': quantity, 'buy_price': buy_price}

# Function to remove stock
def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio.")
    else:
        print("Stock not found in portfolio.")

# Function to fetch real-time stock prices
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    if not data.empty:
        return data['Close'].iloc[-1]  # Last closing price
    else:
        return None

# Function to display portfolio
def display_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return
    
    print("\nYour Portfolio:")
    print(f"{'Stock':<10}{'Qty':<10}{'Buy Price':<12}{'Current Price':<15}{'P/L (%)'}")
    print("-" * 60)
    
    total_invested = 0
    total_current = 0
    
    for symbol, details in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price:
            total_price = details['quantity'] * details['buy_price']
            current_value = details['quantity'] * current_price
            profit_loss = ((current_value - total_price) / total_price) * 100
            total_invested += total_price
            total_current += current_value
            print(f"{symbol:<10}{details['quantity']:<10}{details['buy_price']:<12.2f}{current_price:<15.2f}{profit_loss:.2f}%")
        else:
            print(f"{symbol:<10}{details['quantity']:<10}{details['buy_price']:<12.2f} Data not found")
    
    print("-" * 60)
    total_profit_loss = ((total_current - total_invested) / total_invested) * 100 if total_invested > 0 else 0
    print(f"Total Portfolio Value: ${total_current:.2f}")
    print(f"Total Profit/Loss: {total_profit_loss:.2f}%")

# Main menu
def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter purchase price: "))
            add_stock(symbol, quantity, buy_price)
            print(f"{symbol} added successfully!")
        
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        
        elif choice == "3":
            display_portfolio()
        
        elif choice == "4":
            print("Exiting... Thank you!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Run the portfolio tracker
if __name__ == "__main__":
    main()
