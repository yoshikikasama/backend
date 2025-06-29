from urllib import request

import requests


def retrieve_product_detail(id):
    res = requests.get(f'/api/products/{id}')
    return res.json()