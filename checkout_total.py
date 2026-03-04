def checkout_total_cents(subtotal_cents, discount_percent, tax_percent):
    # calculate discount
    discount = subtotal_cents * discount_percent // 100

    # subtotal after discount
    discount_subtotal = subtotal_cents - discount

    # tax applied to discounted subtotal
    tax = discount_subtotal * tax_percent // 100

    # final total
    total = discount_subtotal + tax

    return total
