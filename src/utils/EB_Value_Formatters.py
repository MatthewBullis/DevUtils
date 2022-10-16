import re

# from utils.EB_Value_Formatters import EB_Offer_Price
class EB_Offer_Price:
    # properties
    price = 0
        
    # class functions:
    def remove_decimal(price):
        if '.' in price:
            print(f"Decimal found in {price}, formatting to whole number")
            price = price.replace('.','')
        else:
            print(f"No decimal found in {price} ")
            price = price
        return price
    # EB_Offer_Price.remove_decimal('12.34')

    def remove_special_characters(value):
        v_string = re.sub('[^A-Za-z0-9 ]+', '', str(value))
        return v_string
    # EB_Offer_Price.remove_special_characters("$12.34")

    

