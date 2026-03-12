
def show_sales(sales):

    print("\nDAILY SALES SUMMARY")
    total_sales = sum(sale["product_sale"] for sale in sales)
    i = 0

    for sale in sales:

        i += 1
        print(f"\nProduct # {i}: {sale['product']}")
        print(f"Total quantity sold: {sale['quantity']}")

    print(f"\nTotal collected: $ {total_sales}")