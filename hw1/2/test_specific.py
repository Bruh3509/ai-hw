from validator_specific import validate_product

def test_validation():
    # Test cases with intentional defects
    test_products = [
        {
            'id': 1,
            'title': '',  # Empty title
            'price': 100,
            'rating': {'rate': 4.5}
        },
        {
            'id': 2,
            'title': 'Test Product',
            'price': -50,  # Negative price
            'rating': {'rate': 4.0}
        },
        {
            'id': 3,
            'title': 'Another Product',
            'price': 200,
            'rating': {'rate': 6.0}  # Rating > 5
        },
        {
            'id': 4,
            'title': None,  # Missing title
            'price': 150,
            'rating': {'rate': 4.0}
        },
        {
            'id': 5,
            'title': 'Product without rating',
            'price': 300,
            # Missing rating
        }
    ]

    print("\n=== Running Validation Tests ===\n")
    
    for product in test_products:
        print(f"Testing Product ID: {product.get('id')}")
        print(f"Input: {product}")
        defects = validate_product(product)
        print(f"Defects found: {defects}\n")

if __name__ == '__main__':
    test_validation() 