
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

    # "return sales" is not necessary (even if execution goes well) because: 

    # Inside the function definition, I am not creating the “sales” list; 
    # I am modifying it (with append), and as the list comes from outside, 
    # “return” is not necessary.

    # If I create and/or modify the “sales” list from inside the function 
    # definition, then I have to return it and do: def sales_registration():
    # BE CAREFUL, LOOK AT HOW IT AFFECTS EVERYTHING ELSE

def sales_continue (sales):
        
    continue_record = input("Continue with registration (YES/NO): ")

    while continue_record in ["y", "Y", "yes", "YES"]:
    # I had: while continue_record.lower() == "yes":
            
        sales_registration(sales)
        continue_record = input("Continue with registration (YES/NO): ")

    # "return sales" unnecessary because of the explanation above

# This is only to try that everything is OK here:
# IF I LEAVE THEM ACTIVE, THE MAIN.PY WILL EXECUTE, BUT INCORRECTLY.
# sales = []
# sales_registration(sales)
# sales_continue(sales)