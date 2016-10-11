
# coding: utf-8

# In[76]:

# [10, 10, ..15, ...]
def find_priceArray(datafeed):
    last_day = 0
    prices = []
    for feed in datafeed:
        feed = feed.split("|")
        if len(feed) == 2:
            day = int(feed[0])
            price = int(feed[1])
            prices.append([day, price])
            if day > last_day:
                last_day = day
    #print prices
    # Fill the price
    full_prices = [None] * (last_day+1)
    
    start = 0
    for [day, price] in prices:
        #print day, price
        while start <= day:
            full_prices[start] = price
            start += 1
    print full_prices
    return full_prices, last_day

# Helper function to find
def is_alert(type, amount, i, day, last_day, prices):
    if type == "SELL":
        # look for price drop if it's a sell
        amount = -amount

    # maximum day we care about
    max_day = day+3
    # find the current price
    current_p = prices[day]

    for d in range(day+1, min(last_day, max_day)+1, 1):
        #print prices[d]
        #print current_p
        price_delta = prices[d] - current_p
        if price_delta * amount >= 5000000:
            return True

    return False

    
# Main function
def findPotentialInsiderTraders(datafeed):
    
    prices, last_day = find_priceArray(datafeed)
    
    res = []
    # build a stock price data feed
    for i, feed in enumerate(datafeed):
        feed = feed.split("|")
        if len(feed) == 4:
            day = int(feed[0])
            trader = feed[1]
            type = feed[2]
            amount = int(feed[3])
            if is_alert(type, amount, i, day, last_day, prices):
                res.append((str(day), trader))
    
    res = list(set(res))
    res.sort(key = lambda x: (x[0], x[1]))
    
    final = []
    for item in res:
        final.append("|".join(item))
    
    return final


# In[80]:

# Test 1
datafeed =[
    "0|10",
    "0|Kristi|BUY|250000",
    "0|Will|BUY|50000",
    "0|Tom|SELL|30000",
    "0|Shilpa|BUY|210000",
    "1|25",
    "1|Shilpa|BUY|100000",
    "2|35",
    "2|Kristi|SELL|200000",
    "3|5",
]


# In[ ]:



