import requests
import json

class Portfolio:
    def __init__(self,api_key):
        self.portfolio ={} 
        self.api_key = api_key

    def add_Stocks(self, symbols , shares):

        if symbols in self.portfolio:
            self.portfolio[symbols] += shares
        else :
            self.portfolio[symbols] = shares         
            
    def remove_stocks (self , symbols) :
        if symbols in self.portfolio:
            del self.portfolio[symbols]
        else :
            print(f"{symbols} not found in the portfolio!")
    # take the api from the ALPHA VANTAGE
    def get_stock_price (self , symbols):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbols}&interval=5min&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        
        try:
            latest_time = list(data['Time Series (5min)'].keys())[0]
            stock_price = float(data['Time Series (5min)'][latest_time]['4. close'])
            return stock_price
        except KeyError:
            print("Error fetching data. Please check the stock symbol or try again later.")
            return None
    
    def display_portfolio (self):
        print("\nCurrent Portfolio :")
        print("---------------------------------------------------------")
        for symbols , shares in self.portfolio.items():
            stock_price = self.get_stock_price(symbols)
            if stock_price is not None :
                total_value = stock_price * shares
                print(f"{symbols}: {shares} shares at ${stock_price:.2f} each, Total Value: ${total_value:.2f}")  
             
            else:
                print(f"{symbols}: {shares} shares (Price unavailable)")    
        print("---------------------------------------------------------")

            
if __name__ == "__main__":
    api_key = input("Enter your Alpha Vantage API key: ")
    tracker = Portfolio(api_key)

    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Exit")
        print(" ")

        choice = input("Enter your choice: ")
        print(" ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            tracker.add_Stocks(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            tracker.remove_stocks(symbol)
        elif choice == "3":
            tracker.display_portfolio()
        elif choice == "4":
            print("GOOD WORK !")
            break
        else:
            print("Invalid choice. Please try again.")       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                          
                