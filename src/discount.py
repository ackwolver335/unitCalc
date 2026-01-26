# Here is another Module in Calculator Library created using Python which will provide the outcomes of Discount
# Following is the class of this one 

"""------------------------------------------ Discount Module  ---------------------------------------------"""

methods = [
    '__init__(self)',
    'final_price(self,orgprice,discount)',
]

class Discount:
    original_price = 0
    discount_percent = 0

    def __init__(self):
        pass

    def final_price(self,org_price,discount):
        discount_price = (discount / 100) * org_price
        final_price = org_price - discount_price
        return final_price