from .calculations import basket_subtotal


def apply_threshold_discount(subtotal, threshold_amount, discount_rate):
    # Identify subtotal and if not compliance = 0
    if type(subtotal) not in (int, float) or subtotal < 0:
        subtotal = 0.0
    if type(threshold_amount) not in (int, float) or threshold_amount < 0:
        threshold_amount = 0.0
    if type(discount_rate) not in (int, float) or discount_rate < 0:
        discount_rate = 0.0

    #if they pass 10 instead of 0.10
    if discount_rate > 1:
        discount_rate = 0.0  #Ignore invalid values
    
    #Apply the discount rate.
    if subtotal >= threshold_amount:
        subtotal = subtotal * (1 - discount_rate)

    return round(subtotal, 2)


def compute_tax(subtotal, tax_rate):
    # Identify subtotal and if not compliance = 0
    if type(subtotal) not in (int, float) or subtotal < 0:
        subtotal = 0.0
    if type(tax_rate) not in (int, float) or tax_rate < 0:
        tax_rate = 0.0
    
    #Rule of tax
    if tax_rate > 1:
        tax_rate = 0.0  #Ignore invalid values
    
    tax = subtotal * tax_rate
    #Subtotal(result) with 2 decimals
    return round(tax, 2)


def grand_total(basket, bogof_items=None, category_discounts=None, threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13):
    #Subtotal of items
    subtotal_items = basket_subtotal(basket, bogof_items, category_discounts)
    
    #Apply discount
    sub_with_discount = apply_threshold_discount(subtotal_items, threshold_amount, threshold_rate)
    tax = compute_tax(sub_with_discount, tax_rate)
    total = sub_with_discount + tax
    
    #Subtotal(result) with 2 decimals
    return round(total, 2)