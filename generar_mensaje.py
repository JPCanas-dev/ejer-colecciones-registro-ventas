from calcular import sales_registration

def show_sales(sales, total_sales):

    print("\nDAILY SALES SUMMARY")

    for sale in sales:

        print(f"\nProduct: {sale['product']}")
        print(f"Total quantity sold: {sale['quantity']}")

    print(f"\nTotal collected: $ {total_sales}")