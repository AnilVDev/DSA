stock_prices = {'march 6': 310.0,
 'march 7': 340.0,
 'march 8': 380.0,
 'march 9': 302.0,
 'march 10': 297.0,
 'march 11': 323.0}
print(stock_prices['march 11'])

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100
print(get_hash('march 15'))

