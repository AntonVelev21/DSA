company_trades = [("AAPL", 100), ("TSLA", 50), ("AAPL", 20), ("MSFT", 120), ("TSLA", 70)]

def top_tickers(trades, k):
    pairs = {}

    for company, trade in trades:
        if company not in pairs:
            pairs[company] = trade
        else:
            pairs[company] += trade

    sorted_pairs = sorted(pairs.items(), key=lambda x: (-(x[1]), x[0]))

    return sorted_pairs[:k][0][0], sorted_pairs[:k][1][0]


print(top_tickers(company_trades, 2))