# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

def calculate_investment():
    portfolio = {}
    total_value = 0

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Invalid input. Quantity must be a number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_value += stock_prices[stock] * quantity

    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}")
    print(f"\nTotal Investment Value: ${total_value}")

    save_choice = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_choice == "yes":
        file_type = input("Save as .txt or .csv? ").lower()
        if file_type == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("--- Portfolio Summary ---\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}\n")
                f.write(f"\nTotal Investment Value: ${total_value}\n")
            print("Portfolio saved to portfolio.txt")
        elif file_type == "csv":
            import csv
            with open("portfolio.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price", "Value"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
                writer.writerow(["Total", "", "", total_value])
            print("Portfolio saved to portfolio.csv")
        else:
            print("Invalid file type. Skipping save.")

calculate_investment()
