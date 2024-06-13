import pandas as pd
from tabulate import tabulate


produtos = [
    {"Nome": "IPad", "Preço": 1200, "Quantidade": 1000},
    {"Nome": "Iphone", "Preço": 3000, "Quantidade": 60},
    {"Nome": "AppleWatch", "Preço": 2600, "Quantidade": 5000},
]

table = pd.DataFrame(produtos)
print(produtos)
print(tabulate(produtos, headers="keys", tablefmt="fancy_grid"))