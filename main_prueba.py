
sales = []
endrecord = 0
i = 0

def sales_registration (endrecord,i):

    while endrecord  == 0:

        print(f"\nProduct # {i + 1}")

        product = input("Enter product name: ")
        price = float(input("Enter unit price $: "))
        quantity = float(input("Enter quantity sold: "))

        sale_dicctionary = {

            "product" : product,
            "price" : price,
            "quantity" : quantity,
            "product_sale" : price * quantity

        }

        sales.append(sale_dicctionary)

        continue_record = input("Continue with registration (YES/NO): ").lower()

        if continue_record == "yes":
            i += 1
        elif continue_record == "no":
            endrecord = 1

    total_sales = sum(sale["product_sale"] for sale in sales)
    return total_sales

def show_sales(total_sales):

    print("\nDAILY SALES SUMMARY")

    for sale in sales:

        print(f"\nProduct: {sale['product']}")
        print(f"Total quantity sold: {sale['quantity']}")

    print(f"\nTotal collected: $ {total_sales}")

total_sales = sales_registration(endrecord,i)
show_sales(total_sales)
