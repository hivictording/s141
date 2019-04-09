# Author: Victor Ding

import json

try:
    with open("products.json","r") as fh_products:
        items_json = fh_products.read()
        items = json.loads(items_json)
except FileNotFoundError:
    exit("Sorry, no goods left in Walmart right now, please visit at a later time......")

for i in items:
    print(items[i])

