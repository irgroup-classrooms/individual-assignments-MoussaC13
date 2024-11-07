import re 


def main():
    
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'

    # Match the regex with the text
    orders = re.findall(regex, text)

    # Print the results
    print(orders)
    
    # 2. Extract all product names
    regex = r'Product: ([^,]+)'

    products = re.findall(regex, text)

    print(products)

    # 3. Extract all prices.
    regex = r'Price: \$(\d+\.\d{2})'

    prices = re.findall(regex, text)

    print(prices)

    # 4. Extract all order dates.
    regex = r'Date: [0-9]{4}-[0-9]{2}-[0-9]{2}'

    dates = re.findall(regex, text)

    print(dates)

    # 5. Find all orders for products priced over $500. (You are allowed to use Python to filter the list.)
    # / No Idea

    # 6. Change the date format to DD/MM/YYYY. (Note the re.sub() method)
    # / No Idea

    # 7. Extract product names that have more than 6 characters.
    product_regex = r'Product: ([^,]+)'

    # Extract all product names
    all_products = re.findall(product_regex, text)

    # Filter products that have more than 6 characters
    long_products = [product for product in all_products if len(product) > 6]

    print(long_products)

# 8. Count the occurrence of each product in the text. (You may want to use the Counter class from the collections package.)
# / No Idea

# 9. Extract the orders with prices ending in .99.
    regex = r'\b\d{2,3}\.99\b'

    prices_with_99 = re.findall(regex, text)

    print("Prices ending in .99:")
    print(prices_with_99)

#10. Find the cheapest product. (You may want to use Python's min() method.)
# / No Idea

if __name__ == '__main__':
    main()
