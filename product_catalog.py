from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  
print("Customer Preferences:", customer_preferences)
# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append(set(product["tags"]))




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    matchCount = 0
    for customer_tag in customer_tags:
        if customer_tag in product_tags:
            matchCount += 1
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return matchCount
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    productMatchList = []
    for product in products:
        matchCount = count_matches(set(product["tags"]), customer_tags)
        productMatchList.append({"name": product["name"], "matchCount": matchCount})

    # Sort the list by match count in descending order
    productMatchList.sort(key=lambda x: x["matchCount"], reverse=True)
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    return productMatchList

    pass



# TODO: Step 7 - Call your function and print the results
'dont like products with 0 matches listed or how jumbled everything is. Hard to reaad'
print("Recommended Products:", recommend_products(products, customer_preferences_set))



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

'(1) '
'In this code, I used for loops, if statements, sets, lists, sorting, and functions. '
'I used for loops to iterate through customer preferences and our products as well as if '
'statements to check for matches between the customer preferences and product tags. '
'I used sets to get rid of duplicates and make it easier to compare tags. '
'I also used functions to organize the code and sorting to put the products in order by most matches.'
'Lists were also used to store customer preferences and the products with their match counts. '

'(2) '
'With 1000 products, I would start by saying make the code more efficient '
'but I am still fairly new to coding and am not sure how or what I would actually change.'
'Other than that though, I hate how the products are presented to the user along with the tags.'
'The information is just jumbled and hard to read. I understand this isnt a website or anything,'
'and that is serves to help me learn and get started but I have issues. I could see this working'
'as one of those filter results tools on search engines or websites. '
'For example, if you type tags into a search bar, you would get a list of products with pictures '
'and their tags at the bottom of the description. You would only display the products that '
'matched because the user does not care about the products that dont match. You could also'
'add all the matches together to display how many products actually match like how Google tells '
'you there are a certain number of results. There could also be a filter system like Facebook Marketplace'
'where you dont have to search anything to get results because you already see products but you have the option '
'to search for things. You could search for items and then narrow that search down by clicking tags in a filter.'
'So yeah, other than boost efficiency, I think changing how the information is presented and allowing users to search and filter the products would make more sense with 1000+ products.'