
def sales_registration (sales):

    product = input("\nEnter product name: ")
    price = float(input("Enter unit price $: "))
    quantity = float(input("Enter quantity sold: "))

    sale_dicctionary = {

        "product" : product,
        "price" : price,
        "quantity" : quantity,
        "product_sale" : price * quantity

    }

    sales.append(sale_dicctionary)
    return sales

def sales_continue (sales):
        
        continue_record = input("Continue with registration (YES/NO): ").lower()

        while continue_record == "yes":

            if continue_record == "yes":
                 
                 sales_registration(sales)
                 continue_record = input("Continue with registration (YES/NO): ").lower()

        # I can only return multiple VALUES this way in Python.
        return sales

# This is only to try that everything is OK here

# sales = []: I can put this at the begining, just for understand the secuence
# sales = sales_registration(sales)
# sales_continue(sales)