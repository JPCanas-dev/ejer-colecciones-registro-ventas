
def sales_registration (sales):

    product = input("\nEnter product name: ")
    price = float(input("Enter unit price $: "))
    quantity = int(input("Enter quantity sold: "))

    sale_dicctionary = {
        "product" : product,
        "price" : price,
        "quantity" : quantity,
        "product_sale" : price * quantity
    }

    sales.append(sale_dicctionary)

def sales_continue (sales):
        
    continue_record = input("Continue with registration (YES/NO): ")

    while continue_record in ["y", "Y", "yes", "YES"]:
    # I had: while continue_record.lower() == "yes":
            
        sales_registration(sales)
        continue_record = input("Continue with registration (YES/NO): ")
        