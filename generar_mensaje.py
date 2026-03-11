
from calcular import sales_registration
from calcular import sales_continue

def show_sales(sales):

    print("\nDAILY SALES SUMMARY")

    # Reserved function sum(): cumulative sum

    # sale is an iterative variable like i in for i in range(), it goes through
    # the entire sales list position by position.

    # And as the list stores dictionaries, sale is also a “dictionary", Never a
    # "number" or anything else

    total_sales = sum(sale["product_sale"] for sale in sales)
    # print(total_sales)

    i = 0

    for sale in sales:

        i += 1
        print(f"\nProduct # {i}")
        print(f"Product: {sale['product']}")
        print(f"Total quantity sold: {sale['quantity']}")

    print(f"\nTotal collected: $ {total_sales}")

# I'm not returning anything, because this is where the program ends.

# This is only to try that everything is OK here

# sales = []
# sales = sales_registration(sales)
# sales = sales_continue(sales)
# show_sales (sales)