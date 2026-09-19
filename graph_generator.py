import matplotlib.pyplot as plt
import yfinance as yf

def gene(name, time):
    stock = yf.Ticker(str(name))
    data = stock.history(period=time)
    close = data["Close"]
    open_price = data["Open"]
    high = data["High"]
    low = data["Low"]
    y = data.index
    hauteur = close - open_price
    couleurs = ["green" if h >= 0 else "red" for h in hauteur]

    plt.figure(figsize=(14, 6))
    plt.vlines(y, low, high, color=couleurs, linewidth=1)
    plt.bar(y, hauteur, bottom=open_price, color=couleurs, width=0.6)
    plt.title(f"{name} - Chandelier")
    return plt.show()

gene("MSFT", "10d")
