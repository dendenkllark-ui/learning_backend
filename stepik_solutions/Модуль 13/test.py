def is_promocode_applicable(order_total, orders_number):
    if order_total > 1000 and orders_number == 0:
        return 'YES'
    else:
        return 'NO'

print(is_promocode_applicable(2499, 1))