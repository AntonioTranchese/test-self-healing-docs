def calculate_total(price, discount=0.10, tax=0.05):
    """Calculates the total price with a discount."""
    discounted = price - (price * discount)
    return discounted + (discounted * tax)
