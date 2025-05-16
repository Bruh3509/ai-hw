import requests
import json
import logging
from datetime import datetime

# Set up logging
def setup_logging():
    # Create logs directory if it doesn't exist
    import os
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Set up logging configuration
    log_filename = f'logs/validation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    return log_filename

def validate_products():
    try:
        # Log API request
        logging.info("Starting API request to https://fakestoreapi.com/products")
        
        # Fetch data from API
        response = requests.get('https://fakestoreapi.com/products')
        
        # Log response status
        logging.info(f"API Response Status Code: {response.status_code}")
        
        if response.status_code != 200:
            error_msg = f"API request failed with status: {response.status_code}"
            logging.error(error_msg)
            raise Exception(error_msg)

        products = response.json()
        logging.info(f"Retrieved {len(products)} products")
        defects = []

        # Validate each product
        for index, product in enumerate(products):
            product_defects = []
            
            logging.info(f"\nValidating Product {index + 1} (ID: {product.get('id', 'Unknown')})")
            logging.debug(f"Raw product data: {json.dumps(product, indent=2)}")

            # 1. Title validation
            if not product.get('title'):
                product_defects.append('Missing title')
            elif not isinstance(product['title'], str):
                product_defects.append('Title is not a string')
            elif not product['title'].strip():
                product_defects.append('Empty title')
            elif len(product['title'].strip()) < 10:
                product_defects.append('Title too short (min 10 characters)')

            # 2. Price validation
            price = product.get('price')
            if price is None:
                product_defects.append('Missing price')
            elif not isinstance(price, (int, float)):
                product_defects.append('Price is not a number')
            elif price < 0:
                product_defects.append('Negative price')
            elif price > 10000:
                product_defects.append('Price exceeds maximum limit (10000)')

            # 3. Rating validation
            rating = product.get('rating', {})
            if not rating:
                product_defects.append('Missing rating')
            else:
                rate = rating.get('rate')
                count = rating.get('count')
                
                if rate is None:
                    product_defects.append('Missing rating value')
                elif not isinstance(rate, (int, float)):
                    product_defects.append('Rating is not a number')
                elif rate < 0 or rate > 5:
                    product_defects.append('Rating out of range (0-5)')
                
                if count is None:
                    product_defects.append('Missing rating count')
                elif not isinstance(count, int):
                    product_defects.append('Rating count is not an integer')
                elif count < 0:
                    product_defects.append('Negative rating count')
                elif count < 10:
                    product_defects.append('Low rating count (< 10)')

            # 4. Category validation
            valid_categories = {
                "electronics", "jewelery", "men's clothing", "women's clothing"
            }
            category = product.get('category')
            if not category:
                product_defects.append('Missing category')
            elif not isinstance(category, str):
                product_defects.append('Category is not a string')
            elif category not in valid_categories:
                product_defects.append(f'Invalid category: {category}')

            # 5. Description validation
            description = product.get('description')
            if not description:
                product_defects.append('Missing description')
            elif not isinstance(description, str):
                product_defects.append('Description is not a string')
            elif len(str(description).strip()) < 20:
                product_defects.append('Description too short (min 20 characters)')

            # Log validation results for this product
            if product_defects:
                defects.append({
                    'id': product.get('id', index),
                    'title': product.get('title', 'Unknown Product'),
                    'defects': product_defects
                })
                logging.warning(f"Product {product.get('id', index)} has defects: {', '.join(product_defects)}")
            else:
                logging.info(f"Product {product.get('id', index)} passed all validations")

        # Log overall results
        logging.info(f"\nValidation completed. Found {len(defects)} products with defects")
        
        return {
            'totalProducts': len(products),
            'defectsFound': len(defects),
            'defects': defects
        }

    except Exception as error:
        logging.error(f"Error during validation: {str(error)}")
        return {
            'error': str(error),
            'defectsFound': 0,
            'defects': []
        }

def main():
    # Setup logging
    log_file = setup_logging()
    logging.info("=== Starting API Validation ===")
    
    # Run validation
    result = validate_products()
    
    if 'error' in result and result['error']:
        logging.error(f"Validation failed: {result['error']}")
        return

    # Log summary
    logging.info("\n=== Validation Summary ===")
    logging.info(f"Total Products: {result['totalProducts']}")
    logging.info(f"Products with Defects: {result['defectsFound']}")
    
    if result['defects']:
        logging.info("\nDefective Products:")
        for item in result['defects']:
            logging.info(f"\nProduct ID: {item['id']}")
            logging.info(f"Title: {item['title']}")
            logging.info(f"Defects Found: {', '.join(item['defects'])}")
    else:
        logging.info("\nNo defects found in the products!")
    
    logging.info(f"\nLog file saved to: {log_file}")

if __name__ == '__main__':
    main() 