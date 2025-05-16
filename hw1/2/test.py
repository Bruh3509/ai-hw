import logging

def validate_product(product):
    """Helper function to validate a single product"""
    defects = []

    # 1. Title validation
    if not product.get('title'):
        defects.append('Missing title')
    elif not isinstance(product['title'], str):
        defects.append('Title is not a string')
    elif not product['title'].strip():
        defects.append('Empty title')
    elif len(product['title'].strip()) < 10:
        defects.append('Title too short (min 10 characters)')

    # 2. Price validation
    price = product.get('price')
    if price is None:
        defects.append('Missing price')
    elif not isinstance(price, (int, float)):
        defects.append('Price is not a number')
    elif price < 0:
        defects.append('Negative price')
    elif price > 10000:
        defects.append('Price exceeds maximum limit (10000)')

    # 3. Rating validation
    rating = product.get('rating', {})
    if not rating:
        defects.append('Missing rating')
    else:
        rate = rating.get('rate')
        count = rating.get('count')
        
        if rate is None:
            defects.append('Missing rating value')
        elif not isinstance(rate, (int, float)):
            defects.append('Rating is not a number')
        elif rate < 0 or rate > 5:
            defects.append('Rating out of range (0-5)')
        
        if count is None:
            defects.append('Missing rating count')
        elif not isinstance(count, int):
            defects.append('Rating count is not an integer')
        elif count < 0:
            defects.append('Negative rating count')
        elif count < 10:
            defects.append('Low rating count (< 10)')

    # 4. Category validation
    valid_categories = {
        "electronics", "jewelery", "men's clothing", "women's clothing"
    }
    category = product.get('category')
    if not category:
        defects.append('Missing category')
    elif not isinstance(category, str):
        defects.append('Category is not a string')
    elif category not in valid_categories:
        defects.append(f'Invalid category: {category}')

    # 5. Description validation
    description = product.get('description')
    if not description:
        defects.append('Missing description')
    elif not isinstance(description, str):
        defects.append('Description is not a string')
    elif len(str(description).strip()) < 20:
        defects.append('Description too short (min 20 characters)')

    return defects

def test_validation():
    """Function to test validation logic with sample data"""
    # Sample test data
    sample_products = [
        {
            # Test 1: Valid product
            'id': 1,
            'title': "Valid Product Name That Is Long Enough",
            'price': 100,
            'description': "This is a valid product description that meets the minimum length requirement.",
            'category': "electronics",
            'rating': {'rate': 4.5, 'count': 120}
        },
        {
            # Test 2: Multiple defects
            'id': 2,
            'title': "Short",  # Too short
            'price': -10,  # Negative
            'description': "Too short",  # Too short
            'category': "invalid category",  # Invalid category
            'rating': {'rate': 6.0, 'count': 5}  # Rate too high, count too low
        },
        {
            # Test 3: Missing fields
            'id': 3,
            'title': "Product With Missing Fields",
            'price': None,  # Missing price
            'category': "electronics"
            # Missing description and rating
        },
        {
            # Test 4: Invalid data types
            'id': 4,
            'title': "Product With Invalid Data Types",
            'price': "100",  # String instead of number
            'description': 12345,  # Number instead of string
            'category': "electronics",
            'rating': {'rate': "4.5", 'count': "100"}  # Strings instead of numbers
        },
        {
            # Test 5: Empty strings
            'id': 5,
            'title': "",  # Empty title
            'price': 50,
            'description': "   ",  # Only whitespace
            'category': "",  # Empty category
            'rating': {'rate': 4.0, 'count': 100}
        }
    ]

    print('\n=== Running Validation Tests ===\n')
    
    for i, product in enumerate(sample_products, 1):
        print(f'Test {i}: {product.get("title", "Unnamed Product")}')
        defects = validate_product(product)
        
        print('Expected defects:')
        if i == 1:
            print('- None (valid product)')
            print('Result:', 'PASS' if not defects else 'FAIL')
        else:
            if i == 2:
                expected = [
                    'Title too short (min 10 characters)',
                    'Negative price',
                    'Description too short (min 20 characters)',
                    'Invalid category: invalid category',
                    'Rating out of range (0-5)',
                    'Low rating count (< 10)'
                ]
            elif i == 3:
                expected = [
                    'Missing price',
                    'Missing description',
                    'Missing rating'
                ]
            elif i == 4:
                expected = [
                    'Price is not a number',
                    'Description is not a string',
                    'Rating is not a number',
                    'Rating count is not an integer'
                ]
            elif i == 5:
                expected = [
                    'Empty title',
                    'Description too short (min 20 characters)',
                    'Invalid category: '
                ]
            
            print('- ' + '\n- '.join(expected))
            print('\nFound defects:')
            print('- ' + '\n- '.join(defects) if defects else 'None')
            
            # Check if all expected defects were found
            all_found = all(exp in defects for exp in expected)
            no_extras = all(found in expected for found in defects)
            print('\nResult:', 'PASS' if all_found and no_extras else 'FAIL')
        
        print('\n' + '-'*50)

if __name__ == '__main__':
    test_validation() 