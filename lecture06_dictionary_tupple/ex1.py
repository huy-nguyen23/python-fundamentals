def fillable(stock, merch, n):
    t=stock.get(merch,0)
    if n<=t:
        return True
    elif n>t:
        return False