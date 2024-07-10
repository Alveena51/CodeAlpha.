#COMMAND TO RUN THIS PROGRAM ========== pip install requests
import requests
import json

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio and self.portfolio[symbol] >= shares:
            self.portfolio[symbol] -= shares
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
        else:
            print(f"Cannot remove {shares} shares of {symbol}. Not enough shares in the portfolio.")

    def get_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        if "Time Series (1min)" in data:
            latest_refresh = data["Meta Data"]["3. Last Refreshed"]
            latest_data = data["Time Series (1min)"][latest_refresh]
            return float(latest_data["1. open"]), float(latest_data["4. close"])
        else:
            print(f"Error fetching data for {symbol}")
            return None, None

    def track_performance(self):
        print("Stock Portfolio Performance:")
        total_value = 0
        for symbol, shares in self.portfolio.items():
            open_price, close_price = self.get_stock_data(symbol)
            if open_price and close_price:
                stock_value = shares * close_price
                total_value += stock_value
                print(f"{symbol}: {shares} shares, Open Price: ${open_price}, Current Price: ${close_price}, Value: ${stock_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == "3":
            portfolio.track_performance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
