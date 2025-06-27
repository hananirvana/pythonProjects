"""
Quote Tracker (market symbols etc.) - A program which can go out and check the current value
of stocks for a list of symbols entered by the user. The user can set how often the stocks
are checked. For CLI, show whether the stock has moved up or down. Optional: If GUI,
the program can show green up and red down arrows to show which direction the stock value has moved.
"""
import yfinance as yf
from Keys import api_keys

q_tracker = {}

def tracker(symbol):
    pfe = yf.Ticker(symbol)
    return pfe.info

def info(data):
    symbol = data["symbol"]
    name = data["shortName"]
    current_price = data["currentPrice"]
    prev_price = data["regularMarketPreviousClose"]
    opening_price = data["regularMarketOpen"]
    day_low = data["regularMarketDayLow"]
    day_high = data["regularMarketDayHigh"]
    volume = data["regularMarketVolume"]
    val_of_company = data["marketCap"]

    return {"symbol": symbol, "name": name, "current_price": current_price, "prev_price": prev_price, "opening_price": opening_price, "day_low": day_low, "day_high": day_high, "volume": volume, "val_of_company": val_of_company}

def change(sym, prev_price, current_price):
    if prev_price < current_price:
        direction = 'UP'
    else:
        direction = 'DOWN'

    return f"{sym} ${current_price} | Direction: {direction}, by {current_price - prev_price}"


if __name__ == '__main__':
    prompt = int(input("Welcome To Quote Tracker v.1! Type 3 to continue. "))
    if prompt == 3:
        sym = str(input("Stock Symbol: "))
        items = tracker(sym)
        infor = info(items)
        old_p = infor["prev_price"]
        cur_p = infor["current_price"]
        symbo = infor["symbol"]
        print(f"{infor['name']}:", change(symbo, old_p, cur_p))
        # print(f"prev price: {old_p}, current: {cur_p}, sym: {sym}")

