import requests
import json
from datetime import datetime

def validate_product(product):
    defects = []
    
    # Title validation
    if not product.get('title') or not product['title'].strip():
        defects.append(f"Empty or missing title")
    
    # Price validation
    price = product.get('price')
    if price is None:
        defects.append("Missing price")
    elif price < 0:
        defects.append(f"Negative price: {price}")
    
    # Rating validation
    rating = product.get('rating', {})
    rate = rating.get('rate')
    if rate is None:
        defects.append("Missing rating")
    elif rate > 5:
        defects.append(f"Rating exceeds maximum (5): {rate}")
    
    return defects

def validate_api():
    print("\n=== Starting API Validation ===\n")
    
    try:
        # Make API request
        response = requests.get('https://fakestoreapi.com/products')
        print(f"API Response Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error: Expected status code 200, got {response.status_code}")
            return
        
        products = response.json()
        print(f"Retrieved {len(products)} products\n")
        
        # Validate each product
        products_with_defects = []
        
        for product in products:
            defects = validate_product(product)
            if defects:
                products_with_defects.append({
                    'id': product.get('id'),
                    'title': product.get('title', 'Unknown'),
                    'defects': defects
                })
        
        # Print results
        print("=== Validation Results ===")
        print(f"Total products checked: {len(products)}")
        print(f"Products with defects: {len(products_with_defects)}")
        
        if products_with_defects:
            print("\nDefective Products:")
            for item in products_with_defects:
                print(f"\nProduct ID: {item['id']}")
                print(f"Title: {item['title']}")
                print(f"Defects: {', '.join(item['defects'])}")
        else:
            print("\nNo defects found!")

    except Exception as e:
        print(f"Error during validation: {str(e)}")

if __name__ == '__main__':
    validate_api() 