
from calcular import sales_registration
from calcular import sales_continue
from generar_mensaje import show_sales

sales = []
sales = sales_registration(sales)
sales = sales_continue(sales)
show_sales (sales)

