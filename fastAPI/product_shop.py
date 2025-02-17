from typing import Optional

from fastapi import FastAPI, HTTPException


app = FastAPI()


sample_products = [
    {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
    },
    {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
    },
    {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
    },
    {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
    },
    {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
    }
]


@app.get('/product/search')
async def search_products(
        keyword: str,
        category: Optional[str] = None,
        limit: int = 10
):
    filtered = [
        p for p in sample_products
        if keyword.lower() in p['name'].lower()
    ]
    if category:
        filtered = [
            p for p in filtered
            if p['category'].lower() == category.lower()
        ]

    return filtered[:limit]


@app.get('/product/{product_id}')
async def show_product(product_id: int):
    for product in sample_products:
        if product['product_id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail='Product not found')

