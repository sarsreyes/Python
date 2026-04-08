from .calculations import item_subtotal
from .discounts import grand_total


def category_breakdown(basket, bogof_items=None, category_discounts=None):
    #Create total dictionary
    category_dictionary = {}
    #Validate data
    if basket is None or type(basket) is not list:
        return category_dictionary

    for products in basket:
        if type(products) is not tuple or len(products) != 4:
            continue #If not compliance continue

        name, quantity, unit_price, category = products
                # Calculate the item subtotal (with all discount applied BOGOF and dicounts)
        elem_basket = item_subtotal(products, bogof_items, category_discounts)
        
        # Accumulate by category
        if type(category) is not str:
            continue
        if category not in category_dictionary:
            category_dictionary[category] = 0.0
        category_dictionary[category] += elem_basket

    # Total with 2 decimals
    for bas_products in list(category_dictionary.keys()):
        category_dictionary[bas_products] = round(category_dictionary[bas_products], 2)

    return category_dictionary


def cheapest_basket(baskets, *, bogof_items=None, category_discounts=None, threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13):
    if baskets is None or type(baskets) is not dict:
        return None
    # Create variables to obatin th cheapest basket
    choose_basket = None
    basket_total = None

    # Identify one by one to find cheapest
    for name in baskets:
        basket = baskets[name]
        total = grand_total(basket, bogof_items=bogof_items, category_discounts=category_discounts, threshold_amount=threshold_amount, threshold_rate=threshold_rate, tax_rate=tax_rate, )
        if basket_total is None or total < basket_total:
            basket_total = total
            choose_basket = name

    return choose_basket
