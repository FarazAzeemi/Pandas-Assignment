import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/Umair115/PIAIC-BATCH-35-Q2/main/Assignment/inventory.csv"
inventory = pd.read_csv(url)
print(inventory.head(10))

staten_island = pd.read_csv(url, nrows = 10)
print(staten_island)
product_request = staten_island['product_description']
print(product_request)
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
print(seed_request)
inventory['in_stock'] = inventory['quantity'] > 0
print(inventory)
inventory['total_value'] = inventory['price'] * inventory['quantity']
print(inventory)
combine_lambda = lambda row:'{} - {}'.format(inventory.product_type, inventory.product_description)
print(combine_lambda(29))
combine_lambda = lambda row:'{} - {} - {} - {} - {} - {}'.format(inventory.product_type, inventory.product_description, inventory.quantity, inventory.price, inventory.in_stock, inventory.total_value)
print(combine_lambda(29))




