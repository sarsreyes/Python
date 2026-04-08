def item_charged_units(item, bogof_items=None): 
#Objective: how many units are charged
    
    #Item has 4 values
    name, quantity, unit_price, category = item
    #Validate logical quantity value
    if type( quantity ) != int or quantity < 0:
        quantity = 0
    items_2x1 = quantity
    # Check if the product is part of the BOGOF (2x1) promotion
    if bogof_items is not None and name in bogof_items:
        items_2x1 = quantity // 2         
        # For every 2 items, only 1 is charged
        #Floor division example 5 // 2 = 2
    return items_2x1


def item_subtotal(item, bogof_items=None, category_discounts=None):
    # Valid basic structure
    if type(item) is not tuple or len(item) != 4:
        return 0.0
    
    name, quantity, unit_price, category = item

    #Valid types min
    if type(name) is not str or type(category) is not str:
        return 0.0
    if type(quantity) is not int:
        return 0.0
    if type(unit_price) not in (int, float):
        return 0.0
    
    #Rule: negatives = 0
    if quantity < 0:
        quantity = 0
    if unit_price < 0:
        unit_price = 0.0   

    #Charged units (BOGOF)
    units = item_charged_units((name, quantity, unit_price, category), bogof_items)
    subtotal = units * unit_price

    #If discount apply (category discount)
    if category_discounts is not None and type(category_discounts) is dict:
        if category in category_discounts:
            discount_cat = category_discounts[category]
            #Validated discount
            if type(discount_cat) in (int, float) and discount_cat > 0:
                subtotal = subtotal * (1 - discount_cat)
            else:
            #If the discount value is invalid, ignore it
                discount_cat = 0
    #Subtotal(result) with 2 decimals
    return round(subtotal, 2)


def basket_subtotal(basket, bogof_items=None, category_discounts=None):
    if basket is None or type(basket) is not list:
        return 0.0
    subtotal = 0.0    
    for item in basket:
        subtotal += item_subtotal(item, bogof_items, category_discounts)
    
    #Subtotal(result) with 2 decimals
    return round(subtotal, 2)