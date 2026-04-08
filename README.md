Grocery Basket Analyzer
Objective
You will design and implement a modular Python package named grocery_toolkit that analyzes the contents of grocery shopping baskets.
The main program main.py (provided to you) will import and test your toolkit.
Your goal is to correctly implement all required modules and functions so that running python main.py produces the expected output.
Provided File
●	main.py: the demo script (you must not modify this file).
When executed, main.py prints results for various test cases using your implemented toolkit. At first, it will not run correctly because the required functions are missing; you must implement all functionalities in the three modules to make it fully work.
You may comment out some test sections in main.py and gradually uncomment them as you complete each part.
Folder Structure
Your project must have the following structure:
assignment1/
├── main.py (this is already given to you)
└── grocery_toolkit/
    ├── __init__.py
    ├── calculations.py
    ├── discounts.py
    └── analysis.py
●	What you need to implement goes into the three .py modules inside the grocery_toolkit package.
●	You must follow the exact folder structure shown above; otherwise, marks will be deducted.
Data Representation
Each item in a basket is represented as a tuple in the following format:
(name, quantity, unit_price, category)
For example: ("banana", 6, 0.39, "produce") means 6 bananas, each priced at $0.39, belonging to the "produce" category.
A basket is a list of such item tuples.
Special rules
●	BOGOF (Buy One Get One Free):
If an item’s name appears in the bogof_items set, only half of its quantity is charged (rounded down).
●	Category discounts:
If a category appears in the category_discounts dictionary, its discount rate (e.g. 0.10 = 10%) is applied to that item’s subtotal.
●	Threshold discount and tax:
○	After all item-level discounts (like BOGOF and category discounts) are applied and the basket subtotal is computed, additional basket-level adjustments are made:
1.	Threshold Discount
○	If the basket’s subtotal is greater than or equal to a set threshold amount ($20 in main.py), an extra percentage discount (10% in main.py) is applied.
2.	Tax Calculation
○	After the threshold discount is applied, tax is added based on the given tax_rate. For example, with a 13% tax rate (0.13 in main.py), the final total = discounted subtotal × 1.13.
Part 1: calculations.py
Implement core item and basket calculations.
Functions to implement:
1.	item_charged_units(item, bogof_items=None)
○	Input: one tuple like ("banana", 6, 0.39, "produce")
○	If the item is in bogof_items, charge only half (round down).
○	Otherwise, charge full quantity.
○	Return the number of charged units as an integer.
2.	item_subtotal(item, bogof_items=None, category_discounts=None)
○	Compute the item’s total cost (subtotal) after:
■	Applying BOGOF discount (if eligible).
■	Applying category discount (if category in category_discounts dict).
○	Return the item’s total rounded to 2 decimals.
3.	basket_subtotal(basket, bogof_items=None, category_discounts=None)
○	Input: list of item tuples.
○	Compute the sum of all item_subtotal() values.
○	Return rounded to 2 decimals.
Part 2: discounts.py
Implement discount and tax logic.
Functions to implement:
1.	apply_threshold_discount(subtotal, threshold_amount, discount_rate)
○	If subtotal ≥ threshold_amount, apply the discount rate.
○	Return discounted subtotal (rounded to 2 decimals).
2.	compute_tax(subtotal, tax_rate)
○	Compute tax on the given subtotal.
○	Return tax amount (rounded to 2 decimals).
3.	grand_total(basket, bogof_items=None, category_discounts=None, threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13)
○	Full pricing pipeline:
1.	Compute subtotal of the basket.
2.	Apply threshold discount.
3.	Compute and add tax.
○	Return final total (rounded to 2 decimals).
○	Important: All parameters after “basket” must be passed as keyword arguments.
Part 3: analysis.py
Implement a few reporting and comparison tools.
Functions to implement:
1.	category_breakdown(basket, bogof_items=None, category_discounts=None)
○	Return a dictionary {category: total_after_discounts}.
○	Important: All parameters after “basket” must be passed as keyword arguments.
2.	cheapest_basket(baskets, bogof_items=None, category_discounts=None, threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13)
○	Input: dictionary of baskets, e.g.
{"BasketA": basket_a, "BasketB": basket_b, "BasketC": basket_c}
○	Return the name of the basket with the lowest grand total (if totals are equal, return the first basket).
○	Important: All parameters after “basket” must be passed as keyword arguments.
Submission
●	You must submit a single .zip file (no .rar or other archive types accepted).
●	Before submitting, test your zip file by extracting it yourself. When extracted, it must contain the top-level folder named assignment1/, which includes all required files and subfolders (See Folder Structure above).
●	Incorrect file/folder structures files will result in mark reduction.
Important Notes
●	Your work must be entirely your own. Do not use AI tools to generate code or comments. Submissions containing AI-generated content will be treated as a violation of academic integrity and will result in disciplinary action.
●	Always round monetary values to two decimals.
●	You are expected to reuse your earlier functions where appropriate. Failure to do so may result in mark reduction.
●	Handle invalid or unexpected inputs safely. Your functions should not crash, instead, return sensible defaults (e.g., 0 or empty results) when data is missing or incorrect.
●	Treat negative values as 0.
●	bogof_items and category_discounts will always be provided, but they may be empty (like empty set or an empty dictionary, meaning no discounts). Your code must handle these cases, and still produce correct results without crashing.
●	The code in main.py already provides example data and constants. Your functions must work correctly with these values as well as other cases.
●	Do not import anything outside the grocery_toolkit package.
●	Place all imports at the top of each file.
●	Use clear, meaningful comments to explain your logic and improve readability. No AI-generated comments.
