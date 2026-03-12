
def show_sales(sales):

    print("\nDAILY SALES SUMMARY")

    # Reserved function sum(): acumulative sum

    # "sale" is an iterative variable like i in "for i in range()", it goes through
    # the entire sales list position by position. 

    # It can have any name, but for convenience it is called “sale”.

    # As the list stores dictionaries, sale is also a “dictionary", never a "number"
    # or anything else

    total_sales = sum(sale["product_sale"] for sale in sales)

    i = 0

    for sale in sales:

        i += 1
        print(f"\nProduct # {i}: {sale['product']}")
        print(f"Total quantity sold: {sale['quantity']}")

    print(f"\nTotal collected: $ {total_sales}")

    # I'm not returning anything, because this is where the program ends.

# This is only to try that everything is OK here:
# IF I LEAVE THEM ACTIVE, THE MAIN.PY WILL EXECUTE, BUT INCORRECTLY.

# from calculate import sales_registration
# from calculate import sales_continue

# sales = []
# sales_registration(sales)
# sales_continue(sales)
# show_sales (sales)